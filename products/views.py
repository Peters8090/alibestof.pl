from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator
from django.views import generic
from django.http import Http404

from .models import Product
from base.models import Configuration
from .forms import ProductSearchForm


def products_list(request, username, page=1):
    products = Product.objects.filter(user__username__exact=username,
                                      published=True)
    if request.GET.get('query') is not None:
        if request.GET.get('query') == "":
            return HttpResponseRedirect(
                reverse('products:products_list', args={username, page}))

        try:
            products = products.filter(pk=int(request.GET.get('query')))
        except ValueError:
            products = products.filter(Q(name__icontains=request.GET.get('query')) |
                                       Q(description__icontains=request.GET.get('query')))

    products_paginator = Paginator(products, Configuration.get_configuration().products_per_page)
    products_paginator_current_page = Paginator(products,
                                                Configuration.get_configuration().products_per_page).get_page(page)
    products = products_paginator.get_page(page).object_list

    product_search_form = ProductSearchForm(request.GET or None)

    context = {
        'username': username,
        'products': products,
        'products_paginator': products_paginator,
        'products_paginator_current_page': products_paginator_current_page,
        'product_search_form': product_search_form,
        'request_text': request.build_absolute_uri().split('/')[-1].translate(str.maketrans('', '', '0123456789')),
    }
    return render(request, 'products/products_list.html', context)


# do not touch, leave it as is!
def products_list_pagination_custom_page_redirect(request, username):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1

    reverse_url = reverse('products:products_list', args=(username, page))
    return redirect(reverse_url + request.GET.get('request_text'))


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if context['product'].published is False:
            raise Http404('No product found matching the query')
        return context

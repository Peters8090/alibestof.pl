from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views import generic
from try_parse.utils import ParseUtils

from base.models import Configuration
from categories.models import Category, Subcategory
from .forms import ProductSearchForm
from .models import Product


def home_page(request):
    return HttpResponseRedirect(
        reverse('products:products_list',
                kwargs={'username': Configuration.get_configuration().home_page_user.username}))


def products_list(request, username, page=1, category=0):
    if not User.objects.filter(username=username):
        raise Http404('No such User found')

    request_text = request.build_absolute_uri().split('/')[-1].translate(str.maketrans('', '', '0123456789'))

    # Find published products of a user
    products = Product.objects.filter(user__username__exact=username,
                                      published=True)

    # Product Filtering - Search
    query = request.GET.get('query')
    if query is not None and query is not "":
        products = products.filter(Q(pk=ParseUtils.try_parse_int(query)[1]) |
                                   Q(name__icontains=query) |
                                   Q(description__icontains=query))
    # Product Filtering - Category
    if int(category) is not 0:
        products = products.filter(category_id__exact=ParseUtils.try_parse_int(category)[1])
    elif 'category' in request.resolver_match.kwargs:
        return HttpResponseRedirect(
            reverse('products:products_list', kwargs={'username': username, 'page': page, }) + request_text)

    products_paginator = Paginator(products, Configuration.get_configuration().products_per_page)
    products_paginator_current_page = Paginator(products,
                                                Configuration.get_configuration().products_per_page).get_page(page)
    products = products_paginator.get_page(page).object_list

    product_search_form = ProductSearchForm(request.GET or None)

    # categories = Category.objects.get_queryset()
    # subcategories = Subcategory.objects.get_queryset()

    context = {
        'username': username,
        'products': products,
        'products_paginator': products_paginator,
        'products_paginator_current_page': products_paginator_current_page,
        'product_search_form': product_search_form,
        'current_category': category,
        # 'categories': categories,
        # 'subcategories': subcategories,
        'query': query,
        'request_text': request_text,
    }
    return render(request, 'products/products_list.html', context)


def products_list_pagination_custom_page_redirect(request, username, category=0):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1

    return redirect(reverse('products:products_list',
                            kwargs={'username': username, 'page': page, 'category': category, }) + request.GET.get(
        'request_text'))


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if context['product'].published is False:
            raise Http404('No product found matching the query')
        context['request'] = self.request
        return context

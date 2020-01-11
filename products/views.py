from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator
from django.views import generic

from .models import Product
from base.models import Configuration
from .forms import ProductSearch


def products_list(request, username, page=1):
    products = Product.objects.filter(user__username__exact=username)
    products_paginator = Paginator(products, Configuration.get_configuration().products_per_page)
    products_paginator_current_page = Paginator(products,
                                                Configuration.get_configuration().products_per_page).get_page(page)

    products = products_paginator.get_page(page).object_list

    form = ProductSearch()

    context = {
        'username': username,
        'products': products,
        'products_paginator': products_paginator,
        'products_paginator_current_page': products_paginator_current_page,
        'form': form,
    }
    return render(request, 'products/products_list.html', context)


def products_list_search(request, username, page=1):
    if request.GET.get('query') is None:
        return HttpResponseRedirect(reverse('products:user_profile', args={username, }))
    else:
        products = Product.objects.filter(Q(name__contains=request.GET.get('query')) |
                                          Q(description__contains=request.GET.get('query')))
        products_paginator = Paginator(products, Configuration.get_configuration().products_per_page)
        products_paginator_current_page = Paginator(products,
                                                    Configuration.get_configuration().products_per_page).get_page(page)

        products = products_paginator.get_page(page).object_list

        form = ProductSearch(request.GET or None)

        context = {
            'username': username,
            'products': products,
            'products_paginator': products_paginator,
            'products_paginator_current_page': products_paginator_current_page,
            'form': form,
        }
        return render(request, 'products/products_list.html', context)


class ProductDetailView(generic.DetailView):
    model = Product

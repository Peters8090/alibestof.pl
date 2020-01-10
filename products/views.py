from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator

from .models import Product
from base.models import Configuration


def user_profile_view(request, username, page=1):
    products = get_list_or_404(Product, user__username__exact=username)
    products = Paginator(products, Configuration.get_configuration().products_per_page).get_page(
        page).object_list
    context = {
        'products': products,
        'username': username,
    }
    return render(request, 'products/user_profile.html', context)


def user_profile_search_view(request, username, page=1):
    if request.GET.get('query') is None:
        return HttpResponseRedirect(reverse('products:user_profile', args={username, }))
    else:
        products = get_list_or_404(
            Product, (
                    Q(name__contains=request.GET.get('query')) |
                    Q(description__contains=request.GET.get('query'))
            )
        )
        products = Paginator(products, Configuration.get_configuration().products_per_page).get_page(
            page).object_list
        context = {
            'products': products,
            'username': username,
        }
        return render(request, 'products/user_profile.html', context)

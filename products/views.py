from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.shortcuts import get_list_or_404

from .models import Product


def user_profile_view(request, username):
    products = get_list_or_404(Product, user__username__exact=username)
    context = {
        'products': products,
        'username': username,
    }
    return render(request, 'products/user_profile.html', context)


def user_profile_search_view(request, username):
    if request.GET.get('query') is None:
        return HttpResponseRedirect(reverse('products:user_profile', args={username, }))
    else:
        products = get_list_or_404(
            Product, (
                    Q(name__contains=request.GET.get('query')) |
                    Q(description__contains=request.GET.get('query'))
            )
        )
        context = {
            'products': products,
            'username': username,
        }
        return render(request, 'products/user_profile.html', context)

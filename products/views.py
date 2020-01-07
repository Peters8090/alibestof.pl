from django.shortcuts import render
from django.views import generic

from .models import Product


def user_profile_view(request, username):
    products = Product.objects.filter(user__username__exact=username)
    context = {
        'products': products,
    }
    return render(request, 'products/user_profile.html', context)

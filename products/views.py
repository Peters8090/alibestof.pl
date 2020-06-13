from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from try_parse.utils import ParseUtils

from base.models import Configuration, Profile
from categories.models import Category, Subcategory
from .forms import ProductSearchForm
from .models import Product


def home_page(request):
    return HttpResponseRedirect(
        reverse('products:products_list',
                kwargs={'username': get_object_or_404(Configuration).home_page_user.username if get_object_or_404(
                    Configuration).home_page_user else None}))


def products_list(request, username, page=1, category=0):
    # 404 if user doesn't exist
    get_object_or_404(User, username=username)

    request_text = '?' + request.GET.urlencode()

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
    if ParseUtils.try_parse_int(category)[1] == 0:
        if 'category' in request.resolver_match.kwargs:
            # No category selected, so clean the url and prevent endless redirects
            return HttpResponseRedirect(
                reverse('products:products_list', kwargs={'username': username, 'page': page, }) + request_text)
    elif category == 'None':
        # Uncategorized category selected
        products = products.filter(category__exact=None)
    else:
        # Some category has been selected
        products = products.filter(category_id__exact=ParseUtils.try_parse_int(category)[1])

    products_paginator = Paginator(products, get_object_or_404(Configuration).products_per_page)
    products_paginator_current_page = Paginator(products,
                                                get_object_or_404(Configuration).products_per_page).get_page(page)
    products = products_paginator.get_page(page).object_list

    product_search_form = ProductSearchForm(request.GET or None)

    home_page_user = get_object_or_404(Configuration).home_page_user

    context = {
        'is_homepage': home_page_user.username == username if home_page_user else False,
        'username': username,
        'products': products,
        'products_paginator': products_paginator,
        'products_paginator_current_page': products_paginator_current_page,
        'product_search_form': product_search_form,
        'current_category': category,
        'categories': Category.objects.get_queryset(),
        'subcategories': Subcategory.objects.get_queryset(),
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


def product_detail(request, pk):
    product = None
    try:
        product = Product.objects.get(pk=pk)
        if not product.published:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('homepage'))

    auth = False
    auth_error = ''
    user_profile_password = None

    try:
        user_profile_password = get_object_or_404(Profile, user__username__exact=product.user.username).password
        if user_profile_password == '' or not user_profile_password:
            raise ObjectDoesNotExist

    except ObjectDoesNotExist:
        auth = True

    try:
        if user_profile_password:
            password_cookie_name = 'password_user_{product_user_id}'.format(product_user_id={product.user.id})
            auth_error_cookie_name = 'auth_error'

            if request.POST.get('password'):
                request.session[password_cookie_name] = request.POST.get('password')

                if request.POST.get('password') != user_profile_password:
                    request.session[auth_error_cookie_name] = 'Wrong password. Get a new one.'

                return HttpResponseRedirect(reverse('products:product_detail', kwargs={'pk': pk}))
            elif request.session[password_cookie_name] == user_profile_password:
                auth = True
            elif request.session[auth_error_cookie_name]:
                auth_error = request.session[auth_error_cookie_name]
                del request.session[auth_error_cookie_name]
    except KeyError:
        pass

    if product.user == request.user or request.user.is_superuser:
        auth = True

    home_page_user = get_object_or_404(Configuration).home_page_user

    context = {
        'product': product,
        'request': request,
        'auth': auth,
        'auth_error': auth_error,
        'is_homepage': home_page_user.username == product.user.username if home_page_user else False,
    }
    return render(request, 'products/product_detail.html', context)

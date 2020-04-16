from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from try_parse.utils import ParseUtils

from base.models import Configuration, UserProfileConfiguration
from categories.models import Category, Subcategory
from .forms import ProductSearchForm
from .models import Product


def home_page(request):
    return HttpResponseRedirect(
        reverse('products:products_list',
                kwargs={'username': Configuration.get_configuration().home_page_user.username}))


def products_list(request, username, page=1, category=0):
    # 404 if user doesn't exist
    get_object_or_404(User, username=username)

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

    products_paginator = Paginator(products, Configuration.get_configuration().products_per_page)
    products_paginator_current_page = Paginator(products,
                                                Configuration.get_configuration().products_per_page).get_page(page)
    products = products_paginator.get_page(page).object_list

    product_search_form = ProductSearchForm(request.GET or None)

    context = {
        'is_homepage': username == Configuration.get_configuration().home_page_user.username,
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
    product = get_object_or_404(Product, pk=pk)
    if not product.published:
        raise Http404('No Product matches the given query.')

    auth = False
    user_profile_password = None

    try:
        user_profile_password = UserProfileConfiguration.get_user_profile_configuration(product.user.username).password
        if user_profile_password == '':
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        auth = True

    if user_profile_password:
        session_cookie_name = 'password_user_{product_user_id}'.format(product_user_id={product.user.id})

        if request.session.get(session_cookie_name) == user_profile_password:
            auth = True
        elif request.POST.get('password'):
            request.session[session_cookie_name] = request.POST.get('password')
            return HttpResponseRedirect(reverse('products:product_detail', kwargs={'pk': pk}))

    if product.user == request.user or request.user.is_superuser:
        auth = True

    context = {
        'product': product,
        'request': request,
        'auth': auth,
        'is_homepage': product.user.username == Configuration.get_configuration().home_page_user.username,
    }
    return render(request, 'products/product_detail.html', context)

from django import template

from categories.models import Category, Subcategory

register = template.Library()


@register.inclusion_tag('categories/show_categories_list.html')
def show_categories(category_url, request_text=''):
    return {
        'categories': Category.objects.get_queryset(),
        'subcategories': Subcategory.objects.get_queryset(),
        'category_url': category_url,
        'request_text': request_text,
    }

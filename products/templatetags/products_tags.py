from django import template

from base.models import Configuration

register = template.Library()


@register.inclusion_tag('products/templatetags/show_profile_info.html')
def show_profile_info(is_homepage, username):
    return {
        'is_homepage': is_homepage,
        'username': username,
    }

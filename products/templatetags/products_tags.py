from django import template

from base.models import Configuration

register = template.Library()


@register.inclusion_tag('products/templatetags/show_profile_info.html')
def show_profile_info(username):
    return {
        'is_homepage': username == Configuration.get_configuration().home_page_user.username,
        'username': username,
    }

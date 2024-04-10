from django import template
from wagtail.models import Site
from ..models import Menu, Footer

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    try:
        menu = Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return None
    return menu

@register.simple_tag()
def get_homepage():
    return Site.objects.get(is_default_site=True).root_page

@register.simple_tag()
def get_footer(slug):
    try:
        footer = Footer.objects.get(slug=slug)
    except Footer.DoesNotExist:
        return None
    return footer
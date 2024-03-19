from home.models import Header
from django import template

register = template.Library()

@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header_tag(context):
    return {'request': context['request'],
            'header': Header.objects.first()
            }
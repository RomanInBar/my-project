
from django import template

register = template.Library()

@register.filter(name='first_remove')
def first_remove(value):
    return value[1:]


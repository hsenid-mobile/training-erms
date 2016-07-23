from django import template

register = template.Library()


@register.filter(name = 'substract')
def subtract(value, arg):
    return value - arg
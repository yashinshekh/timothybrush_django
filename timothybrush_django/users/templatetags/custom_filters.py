from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the value by the argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return None

@register.filter
def split(value, key):
    """
    Returns the value turned into a list.
    """
    return value.split(key)


@register.filter
def cut(value, arg):
    """Removes all values of arg from the given string."""
    return value.replace(arg, '')


from django import template

register = template.Library()


@register.filter(name='addcss')
def add_attributes(field, css):
    """Adds CSS attributes for bootstrap compatibility"""
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v
            return field.as_widget(attrs=attrs)


@register.filter
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, ', ')

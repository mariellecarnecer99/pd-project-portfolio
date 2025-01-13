from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, class_name):
    # Check if the field is a form field object, not just a string
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={'class': class_name})
    return field

from django import template
register = template.Library()

@register.filter
def temp(temp):
    print(True)
    return (float(temp) * (9/5)) + 32
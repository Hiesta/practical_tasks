from django import template

register = template.Library()

code_symbols = {
    'rub': 'P',
    'usd': '$',
}


@register.filter()
def currency(value, code="rub"):
    return f'{value} {code_symbols[code]}'

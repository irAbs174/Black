from django import template
from product.models import Product


register = template.Library()

@register.inclusion_tag('index/index.html', takes_context=True)
def product(context):
    return {
        'products': Product.objects.all(),
        'request': context['request'],
    }
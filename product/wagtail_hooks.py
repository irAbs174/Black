from django.urls import path
from wagtail import hooks

from .views import product_brands_component


@hooks.register('register_admin_urls')
def register_products_admin_url():
    return [
        path('ProductBrands/', product_brands_component, name='product_brands'),
    ]
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from .models import Product, ProductVisit

class ProductAdmin(ModelAdmin):
    model = Product
    base_url_path = 'products'
    menu_label = 'محصولات' 
    menu_icon = 'desktop'
    menu_order = 400 
    add_to_settings_menu = False  
    exclude_from_explorer = False
    add_to_admin_menu = True 
    list_display = ['product_title', 'price','image','quantity']
    list_filter = ('collection', 'brand', 'is_active','author')
    search_fields = ('product_title','price')


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(ProductAdmin)
'''
modeladmin_register(ProductTag)
modeladmin_register(ProductVisit)
modeladmin_register(ProductGallery)
'''
from django.db import models
from django.urls import reverse
from django.template.response import TemplateResponse
from wagtail.models import Page, PageManager, ClusterableModel, Orderable
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from django.utils import timezone
from index.extensions.jalali_converter import jalali_converter as jConvert
from users.models import CustomUser as User


class ProductPageManager(PageManager):
    pass


@register_snippet
class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='یک مجموعه برای برند انتخاب کنید',
    )
    url_title = models.CharField(max_length=300, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند محصول'
        verbose_name_plural = 'برند محصولات'

    def __str__(self):
        return self.title


@register_snippet
class ProductColor(models.Model):
    color = models.CharField(max_length=10)
    pquantity = models.IntegerField(verbose_name='تعداد رنگ بندی :')
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='یک مجموعه برای رنگ بندی انتخاب کنید',
    )

    def __str__(self):
        return self.color


    class Meta:
        verbose_name = 'رنگ بندی'
        verbose_name_plural = 'رنگ بندی محصولات'


class ProductIndex(Page):
    intro = RichTextField(blank=True, verbose_name='نام صفحه محصولات سایت')

    objects = ProductPageManager()

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    class Meta:
        verbose_name = 'صفحه محصولات'


@register_snippet
class Product(Page):
    date_create = models.DateTimeField(default=timezone.now)
    product_title = models.CharField(max_length=300, verbose_name='نام و مدل محصول', null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey(
        'wagtailcore.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='یک مجموعه برای کالا انتخاب کنید',
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='تصویر محصول',
        help_text='انتخاب تصویر شاخص برای کالا',
        )
    date = models.DateTimeField("Post date",default=timezone.now)
    brand = models.ForeignKey('ProductBrand', on_delete=models.SET_NULL, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت',blank=False, null=False)
    short_description = models.CharField(max_length=360, db_index=True, null=True, blank=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True, null=True, blank=True)
    quantity = models.IntegerField(verbose_name='تعداد محصول',null=False, )
    colors = models.OneToOneField(ProductColor, null=True, blank=True, verbose_name='رنگ بندی محصول :', on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال', blank=False, null=False)
    is_available = models.BooleanField(default=True, verbose_name='موجودی / عدم موجودی', blank=False, null=False)
    product_visit = models.OneToOneField('ProductVisit', on_delete=models.SET_NULL, verbose_name='بازدید محصول', null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('product_title'),
        FieldPanel('brand'),
        FieldPanel('price'),
        FieldPanel('image'),
        FieldPanel('quantity'),
        FieldPanel('short_description'),
        FieldPanel('description'),
        FieldPanel('colors'),
        FieldPanel('is_active'),
        FieldPanel('categories'),
        ]

    def get_context(self, request,*args, **kwargs):
        context = super().get_context(request,*args, **kwargs)
        loaded_product = Product.objects.all()
        context['products'] = loaded_product if loaded_product is not None else 0
        return context

    def get_template(self, request, *args, **kargs):
        return 'index/index.html'

    def server(self, request, *args, **kargs):
        return TemplateResponse(
            request,
            self.get_template(request, *args, **kargs),
            self.get_context(request, *args, **kargs)
        )

    def jpub(self):
        return jConvert(self.date)
    
    jpub.short_description = 'زمان انتشار'

    def sell(self, quantity):
        if self.is_available and self.quantity >= quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.is_available = False
            self.save()
            return True
        else:
            return False

    def restock(self, quantity):
        self.quantity += quantity
        if self.quantity > 0:
            self.is_available = True
        self.save()

    def get_colors(self):
        return ", ".join([ProductColor.name for color in self.colors.all]) if self.colors.exists() else "محصول بدون رنگ بندی است"

    def save(self, *args, **kwargs):
        if not self.is_available:
            self.available = False
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'محصولات'
        

class ProductVisit(models.Model):
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='کاربر', on_delete=models.CASCADE)
    visit = models.IntegerField(verbose_name='بازدید محصول', null=True, blank=True)

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید کالا'
        verbose_name_plural = 'بازدیدهای محصولات'


class Inventory(models.Model):
    products = models.ManyToManyField(Product)

    def sell_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            return product.sell(quantity)
        except Product.DoesNotExist:
            return False

    def restock_product(self, product_id, quantity):
        try:
            product = self.products.get(id=product_id)
            product.restock(quantity)
            return True
        except Product.DoesNotExist:
            return False

    class Meta:
        verbose_name = 'انبار کالا'
        verbose_name_plural = 'انبار کالا'
"""
2020 Black
developer : #ABS
"""

# Import all requirements
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.snippets.models import register_snippet
from wagtail.models import Page, PageManager
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from rest_framework.fields import Field
from taggit.forms import TagField
from wagtail.api import APIField
from wagtail.search import index
from django.db import models

# INDEX PAGE MANAGER
class IndexPageManager(PageManager):
    '''
    DEVELOPMENT : #ABS
     '''
    pass


# Index Child Page Serializer
class IndexChildPageSerializer(Field):
    ''' Serialize model => API | JSON '''
    def to_representation(self, value):
        return [
            {
                'id' : child.id,
                'slug' : child.slug,
                'seo_title' : child.seo_title,
                'title' : child.title,
            }for child in value
        ]


# Index class
class Index(Page):
    body = RichTextField(blank=True)

    objects = IndexPageManager()

    max_count = 1

    parent_page_types = []

    subpage_types = ['blog.BlogIndex',
    'blog.BlogPage',
    'product.Product',
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    api_fields = [
        APIField("get_child_pages", serializer=IndexChildPageSerializer()),
    ]

    @property
    def get_child_pages(self):
        return self.get_children().public().live()

    def get_context(self, request, *args, **kwargs):
        """Send context(Like blog posts) for template"""
        #context = super().get_context(request, *args, **kwargs)
        # Get all posts
        #all_posts = BlogPage.objects.live().public().order_by('-first_published_at')
        pass

    class Meta:
        verbose_name = "خانه"
 

# FOOTER LINK BOX
class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


# FOOTER LINK
class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


# SITE SLIDER
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title


# SITE BANNER
class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list = 'product_list', 'صفحه لیست محصولات',
        product_detail = 'product_detail', 'صفحه ی جزییات محصولات',
        about_us = 'about_us', 'درباره ما'

    title = models.CharField(max_length=200, verbose_name='عنوان بنر')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/banners', verbose_name='تصویر بنر')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنرهای تبلیغاتی'
"""
2020 Black
developer : #ABS
"""

# Import all requirements
from django.db import models
from wagtail.models import Page, PageManager
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase #from wagtail.images
from django.utils import timezone
from index.extensions.jalali_converter import jalali_converter as jConvert
from users.models import CustomUser as User


class BlogPageManager(PageManager):
    pass


# blog app index model
class BlogIndex(Page):
    intro = RichTextField(blank=True, verbose_name='نام صفحه وبلاگ سایت')

    objects = BlogPageManager()

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    class Meta:
        verbose_name = 'صفحه اصلی وبلاگ'


# blog page model
class BlogPage(Page):
    owner: models.ForeignKey(User, blank=True, on_delete=models.SET_NULL)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='تصویر شاخص پست',
        )
    intro = models.CharField(max_length=25, verbose_name='توضیحات ابتدایی راجب پست')
    date = models.DateTimeField("Post date",default=timezone.now)
    body = RichTextField(blank=True, verbose_name='محتوای پست')
    description = models.CharField(max_length=25, verbose_name='توضیحات کامل پست')
    categories = models.OneToOneField('category.Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='دسته بندی پست')
    
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('image'),
        FieldPanel('intro'),
        FieldPanel('description'),
        FieldPanel('categories'),
    ]

    class Meta:
        verbose_name = 'پست وبلاگ'
        verbose_name_plural = 'پست های وبلاگ'

    # Jalali calculator

    def jpub(self):
        return jConvert(self.date)
    
    jpub.short_description = 'زمان انتشار'

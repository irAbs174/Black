
from django.db import models
from wagtail.models import Page, PageManager
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.images.models import Image


class CategoryPageManager(PageManager):
    ''' Category Page Manager '''
    pass


# Index class
class CategoryIndex(Page):
    body = RichTextField(blank=True, verbose_name='عنوان صفحه دسته بندی ها')
    objects = CategoryPageManager()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


    class Meta:
        verbose_name_plural = 'صفحه دسته بندی ها'
        

@register_snippet
class Category(Page):
    name = models.CharField(max_length=255, verbose_name='عنوان دسته بندی')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد دسته بندی')

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]

    panels = [
        FieldPanel('name'),
        FieldPanel('is_active'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
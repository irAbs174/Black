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
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.contrib.routable_page.models import RoutablePageMixin
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase #from wagtail.images
from django.utils import timezone
from index.extensions.jalali_converter import jalali_converter as jConvert
from users.models import CustomUser as User


class BlogPageManager(PageManager):
    pass


# blog app index model
class BlogIndex(Page, RoutablePageMixin):
    intro = RichTextField(blank=True, verbose_name='نام صفحه وبلاگ سایت')

    objects = BlogPageManager()

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = ['blog.BlogPage']
    parent_page_types = ['index.Index']

    @property
    def get_child_pages(self):
        return self.get_children().public().live()

    def get_context(self, request, *args, **kwargs):
        """Send context(Like blog posts) for template"""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')

        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_posts = all_posts.filter(tags__slug__in=[tags])

        # Paginate all posts by 6 per page
        paginator = Paginator(all_posts, 6)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        return context

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

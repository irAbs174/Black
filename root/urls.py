"""
2020 Black
root URL configuration
developer : #ABS
"""

# Import all requirements
from django.urls import include, path, re_path
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
import os.path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls


# url routing configuration
urlpatterns = [
    path('uniqueAdmin/', admin.site.urls),
    path('UNIQUEADMINISTRATOR/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('accounts/', include('allauth.urls')),
    
    re_path(r'', include(wagtail_urls)),
]

# Custom static & storage files configuration
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'blog/images/favicon.ico'))
]

# Add the 404-500 error view
handler404 = 'index.views.page_not_found_error'
handler500 = 'index.views.server_error'
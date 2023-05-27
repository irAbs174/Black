"""
2020 Black
developer : #ABS
"""

# Import all requirements
from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from .models import BlogPage


# class BlogPageAdmin
class BlogPageAdmin(admin.ModelAdmin):
    list_display = ('jpub', 'intro', 'body',)


# register admin
admin.site.register(BlogPage, BlogPageAdmin)
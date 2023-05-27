"""
2020 Black
developer : #ABS
"""

# Import all requirements
from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from .models import BlogPage


# blog page form
class BlogPageFrom(forms.ModelForm):
    
    class meta:
        model = BlogPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BlogPageForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('تاریخ انتشار'), widget=AdminJalaliDateWidget)

    
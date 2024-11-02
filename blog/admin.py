from django.contrib import admin
from . import models
from django import forms

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Administration"
    site_title = "Blog Admin Portal"
    index_title = "Welcome to Blog Portal"

blog_site = BlogAdminArea(name='blogadmin')

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Section 1', {
            'fields': ('title', 'content')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('author', 'category'),
        }),
    )

class Category(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.fields['name'].help_text = 'New Category Name'
    class  Meta:
        model = models.Category
        exclude = ('slug',)

class CatagoryAdminForm(admin.ModelAdmin):
    form = Category

admin.site.register(models.post, PostAdmin)
admin.site.register(models.Category, CatagoryAdminForm)
blog_site.register(models.post)

from django.contrib import admin
from . import models

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Administration"
    site_title = "Blog Admin Portal"
    index_title = "Welcome to Blog Portal"

blog_site = BlogAdminArea(name='blogadmin')

admin.site.register(models.post)
admin.site.register(models.Category)
blog_site.register(models.post)

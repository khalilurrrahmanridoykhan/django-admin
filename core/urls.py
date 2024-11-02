
from django.contrib import admin
from django.urls import path
from blog.admin import blog_site
from bookstore.admin import bookstore_site
from frondend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
    path('bookstoreadmin/', bookstore_site.urls),
    path('', home, name='home' )
]

admin.site.site_header = "Core Administration"
admin.site.site_title = "Core Admin Portal"
admin.site.index_title = "Welcome to Core Portal"

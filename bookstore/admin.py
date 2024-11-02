from django.contrib import admin
from . import models


class BookstoreAdminArea(admin.AdminSite):
    site_header = "Bookstore Administration"
    site_title = "Bookstore Admin Portal"
    index_title = "Welcome to Bookstore Portal"

bookstore_site = BookstoreAdminArea(name='bookstoreadmin')

class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', ('price', 'stock')]

admin.site.register(models.Book,BookAdmin)
bookstore_site.register(models.Book)
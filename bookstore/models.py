from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, help_text='Maximum 100 characters')
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.title

from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField (max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name







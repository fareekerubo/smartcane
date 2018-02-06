from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'price')
    list_filter = ('created', 'updated')
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

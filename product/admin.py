from django.contrib import admin
from .models import Product, Brand, ProductImages, Review

# Register your models here.



class ProductImagesTabular(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'subtitle', 'flag']
    list_filter = ['name', 'brand', 'subtitle', 'flag']
    search_fields = ['name', 'subtitle', 'flag', 'description']
    inlines = [ProductImagesTabular]
 




admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(ProductImages)
admin.site.register(Review)
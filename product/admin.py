from django.contrib import admin
from .models import Product, Brand, ProductImages, Review

# Register your models here.



class ProductImagesTabular(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'subtitle', 'flag']
    list_filter = ['name', 'brand', 'subtitle', 'flag']
    search_fields = ['name', 'subtitle', 'flag', 'brand']
    list_per_page = 500
    inlines = [ProductImagesTabular]
 

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20 




admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductImages)
admin.site.register(Review)
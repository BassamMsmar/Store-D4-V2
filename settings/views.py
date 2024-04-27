from django.shortcuts import render
from product.models import Product, Brand, Review, Categories
from django.db.models import Count
from django.views.decorators.cache import cache_page

# Create your views here.


def home(request):
       brands = Brand.objects.all().annotate(brand_count=Count('product_brand'))
       categories = Categories.objects.all().annotate(categories_count=Count('product_categories'))
       sale_products = Product.objects.filter(flag='sale')[:10] 
       feature_products = Product.objects.filter(flag='feature')[:5]
       new_products = Product.objects.filter(flag='new')[:6] 
       reviwes = Review.objects.all()[:10] 



       return render(request, 'settings/home.html', {
           'brands': brands,
           'categories': categories,
           'sale_products': sale_products,
           'new_products': new_products,
           'feature_products': feature_products,
           'reviews': reviwes
       })
from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count
from django.db.models.aggregates import Avg

from .models import Product, Brand, Review, ProductImages
# Create your views here.


class ProductList(ListView):
    model = Product
    queryset = Product.objects.annotate(product_reviews=Count('review_product'))
    paginate_by = 20


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(ave_rate=Avg('review_product__rate'))
        return queryset
    


class ProductDetail(DetailView):
    model =Product
    queryset = Product.objects.annotate(product_reviews=Count('review_product'))



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    






class BrandList(ListView):
    model = Brand    #context : object_list, model_list
    paginate_by = 20
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
 




class BrandDetail(ListView):
    model = Product     #context : object_list, model_list
    template_name = 'product/brand_detail.html'


    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand) 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.annotate(product_count=Count('product_brand')).get(slug=self.kwargs['slug'])
        return context
    























def queryset_debug(request):
    # products = Product.objects.select_related('brand').all()
    products = Product.objects.filter(brand__name='Apple')

    return render(request, 'product/debug.html', {'products':products})
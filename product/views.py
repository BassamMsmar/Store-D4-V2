from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Brand, Review, ProductImages
# Create your views here.

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model =Product


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["reviews"] = Review.objects.filter(product=self.get_object())
    #     context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
    #     return context
    

class BrandList(ListView):
    model = Brand    #context : object_list, model_list
    paginate_by = 20





class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = Product.objects.all().filter(brand=self.get_object())
        return context
    

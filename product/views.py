from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Brand, Review, ProductImages
# Create your views here.

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model =Product


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ProductImages"] = ProductImages
        return context
    


class BrandList(ListView):
    model = Brand

class BrandDetail(DetailView):
    model = Brand
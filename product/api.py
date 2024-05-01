from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer, BrandSerializer, CategoriesSerializer

from .models import Product, Review, Brand, Categories



class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandListApi(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoriesListApi(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CategoriesDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
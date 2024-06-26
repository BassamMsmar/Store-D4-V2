from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import ProductListSerializer, ProductDetailsSerializer, BrandListSerializer, BrandDetailsSerializer, CategoriesListSerializer, CategoriesDetailsSerializer
from .pagination import MyPagination
from .models import Product, Review, Brand, Categories



class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['categories', 'brand']
    search_fields = ['name']
    ordering_fields = ['create_at']
    pagination_class = MyPagination
    


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer


class ProductCreateApi(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer

    def post(self, request, *args, **kwargs):
        print ("post")


class BrandListApi(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailsSerializer


class CategoriesListApi(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesListSerializer

class CategoriesDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesDetailsSerializer
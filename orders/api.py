from rest_framework import generics 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Cart, CartDetail, Order, OrderDetail
from .serializers import CartSerializer
from product.models import Product



class CartListApi(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        print('bassam get')
      

    def post(self, request, *args, **kwargs):
        print('bassam post')
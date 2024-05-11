from rest_framework import generics 
from .models import Cart, CartDetail, Order, OrderDetail
from .serializers import CartSerializer



class CartListApi(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
from rest_framework import serializers
from .models import Order, OrderDetail, Coupon, Cart, CartDetail




class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'

        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetailSerializer
        fields = '__all__'



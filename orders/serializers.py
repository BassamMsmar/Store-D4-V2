from rest_framework import serializers
from .models import Cart , CartDetail , Order , OrderDetail 


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'
        
        
class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = '__all__'

    def get_name(self, obj):
        return 'bassam'

    def get_age(self, obj):
        return 22
        
        

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
        
        
class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
        
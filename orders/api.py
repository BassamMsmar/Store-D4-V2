from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import CartDetailSerializer, CartSerializer



from .models import Cart , CartDetail , Order , OrderDetail
from product.models import Product
class CartCreateUpdateDelete(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user=user, status='InProgress')
        date = CartSerializer(cart).data
        return Response(date)
    
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity'])

        cart, created = Cart.objects.get_or_create(user=user, status='InProgress')
        cart_detail , created = CartDetail.objects.get_or_create(cart=cart, product=product)

        cart_detail.quantity = quantity
        cart_detail.total = round(product.price * cart_detail.quantity,2)
        cart_detail.save()

        data = CartSerializer(cart).data

        return Response({'message':'cart was updated successfully', 'data':data})



        
    

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = CartDetail.objects.get(id=request.data['item_id']) 
        product.delete()

        cart, created = Cart.objects.get_or_create(user=user, status='InProgress')
        date = CartSerializer(cart).data
        return Response({'massage':'deleted successfully', 'cart':date})

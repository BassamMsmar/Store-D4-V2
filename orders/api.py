from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import CartDetailSerializer, CartSerializer



from .models import Cart , CartDetail , Order , OrderDetail

class CartCreateUpdateDelete(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart, created = Cart.objects.get_or_create(user=user, status='InProgress')
        date = CartSerializer(cart).data
        return Response(date)
    

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = CartDetail.objects.get(id=request.data['item_id']) 
        product.delete()

        cart, created = Cart.objects.get_or_create(user=user, status='InProgress')
        date = CartSerializer(cart).data
        return Response({'massage':'deleted successfully', 'cart':date})
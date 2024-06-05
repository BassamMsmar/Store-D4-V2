from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

from product.models import Product


from .models import Cart, CartDetail, Order

# Create your views here.
 

class OrderList(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 10 


    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset

def add_to_cart(request, pk):
    quantity = request.POST['quantity']
    product = Product.objects.get(pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user, status='InProgress')

    cart_detail, created = CartDetail.objects.get_or_create(cart=cart, product=product)
    cart_detail.quantity = quantity
    cart_detail.total =round(int(quantity) * cart_detail.product.price, 2) 
    cart_detail.save()

    return redirect(f'/product/{product.slug}')

def delete_from_cart(request, pk):
    cart_detail = CartDetail.objects.get(pk=pk)
    cart_detail.delete()
    return redirect('/product')

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user, status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)

    if request.method == 'POST':
        pass


    context = {'cart':cart,
               'cart_detail':cart_detail}


    return render(request, 'orders/checkout.html', context)
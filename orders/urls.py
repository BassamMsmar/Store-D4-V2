from django.urls import path
from .views import OrderList, checkout, add_to_cart, delete_from_cart
from .api import CartListApi


app_name = 'order'
urlpatterns = [
    path('', OrderList.as_view() ),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:pk>/', delete_from_cart, name='delete_from_cart'),
    path('checkout/', checkout, name='checkout'),


    #api
    path('api/cart/', CartListApi.as_view(), name='cart_api'),
]

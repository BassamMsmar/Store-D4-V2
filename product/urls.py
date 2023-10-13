from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail

urlpatterns = [
    path('',ProductList.as_view()),
    path('<int:pk>',ProductDetail.as_view()),

    path('brand',BrandList.as_view()),
    path('brand/<int:pk>',BrandDetail.as_view()),
]

from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, queryset_debug, add_review, ProductListByCategory
from .api import ProductListApi, ProductDetailApi, BrandListApi, BrandDetailApi, CategoriesListApi, CategoriesDetailApi
from . import api
urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<str:slug>', ProductDetail.as_view(), name='product_detail'),
    path('<str:slug>/add_review', add_review, name='add_review'),

    path('debug/', queryset_debug, name='queryset_debug'),

    path('brands/', BrandList.as_view(), name='brand_list'), 
    path('brands/<slug:slug>', BrandDetail.as_view(), name='brand_details'), 

    path('categories/<int:pk>', ProductListByCategory.as_view(), name='products_list_by_category'), 


    #api
    path('api/list/', ProductListApi.as_view(), name='api_product_list'),
    path('api/list/<int:pk>', ProductDetailApi.as_view(), name='api_product_detail'),

    path('api/create/', api.ProductCreateApi.as_view(), name='api_product_create'),

    path('brand/api/list/', BrandListApi.as_view(), name='api_brand_list'),
    path('brand/api/list/<int:pk>/', BrandDetailApi.as_view(), name='api_brand_detail'),

    path('categories/api/list/', CategoriesListApi.as_view(), name='api_categories_list'),
    path('categories/api/list/<int:pk>/', CategoriesDetailApi.as_view(), name='api_categories_detail'),
]

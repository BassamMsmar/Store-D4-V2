from rest_framework import serializers
from django.db.models.aggregates import Avg

from .models import Product, Brand, Categories



class BrandListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = '__all__'


class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categories
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    brand = serializers.StringRelatedField()
    categories = serializers.StringRelatedField()

    class Meta: 
        model = Product
        fields = '__all__'

    def get_avg_rate(self, product):
        avg = product.review_product.aggregate(rate_ave=Avg('rate'))
        if avg['rate_ave'] is None:
            return 0
        return avg['rate_ave']

    def get_reviews_count(self, product):
        return product.review_product.count()
    

  
class ProductDetailsSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Product
        fields = '__all__'

    

class BrandListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = '__all__'


class BrandDetailsSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(source='product_brand', many=True)

    class Meta: 
        model = Brand
        fields = '__all__'


class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categories
        fields = '__all__'

class CategoriesDetailsSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(source='product_categories', many=True)

    class Meta: 
        model = Categories
        fields = '__all__'





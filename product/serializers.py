from rest_framework import serializers
from django.db.models.aggregates import Avg
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

from .models import Product, Brand, Categories, Review



class BrandListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = '__all__'


class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categories
        fields = '__all__'


class ProductListSerializer(TaggitSerializer, serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    brand = serializers.StringRelatedField()
    categories = serializers.StringRelatedField()
    tags = TagListSerializerField()

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
    

class ReviewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductDetailsSerializer(TaggitSerializer, serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    brand = serializers.StringRelatedField()
    categories = serializers.StringRelatedField()
    review_product = ReviewProductSerializer(many=True)
    tags = TagListSerializerField()


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





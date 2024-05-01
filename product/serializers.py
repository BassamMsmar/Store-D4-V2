from rest_framework import serializers
from .models import Product, Brand, Categories

class ProductSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Brand
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Categories
        fields = '__all__'





from rest_framework import serializers
from .models import Category, Title, Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
         fields = ('name', 'slug')
         model = Category


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
         fields = ('__all__')
         model = Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
         fields = ('name', 'slug')
         model = Genre

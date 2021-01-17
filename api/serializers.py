from rest_framework import serializers
from .models import Category, Title, Genre, GenreTitle


class CategorySerializer(serializers.ModelSerializer):
    pass


class TitleSerializer(serializers.ModelSerializer):
    pass


class GenreSerializer(serializers.ModelSerializer):
    pass


class GenreTitleSerializer(serializers.ModelSerializer):
    pass

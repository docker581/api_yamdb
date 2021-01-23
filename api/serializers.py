from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import (
    Category, 
    Title,
    Genre, 
    Review,
    Comment,
)


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


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        exclude = ('review_id', )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        exclude = ('title_id', )

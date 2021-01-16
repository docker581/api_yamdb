from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Title, Genre, GenreTitle
from .serializers import CategorySerializer, TitleSerializer, GenreSerializer, GenreTitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class CurrentCategoryViewSet(viewsets.ModelViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    pass


class CurrentTitleViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class CurrentGenreViewSet(viewsets.ModelViewSet):
    pass

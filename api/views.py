from rest_framework import generics, viewsets, status, filters, permissions
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import get_object_or_404
from .models import Category, Title, Genre, GenreTitle
from .serializers import CategorySerializer, TitleSerializer, GenreSerializer
from .permissions import IsSuperuserPermissionOrReadOnly


class CategoryViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserPermissionOrReadOnly & IsAuthenticatedOrReadOnly] 
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class GenreViewSet(viewsets.ModelViewSet):    
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsSuperuserPermissionOrReadOnly] 
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    

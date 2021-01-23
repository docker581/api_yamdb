from rest_framework import generics, viewsets, status, filters, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404
from .models import Category, Title, Genre, GenreTitle
from .serializers import CategorySerializer, TitleSerializer, GenreSerializer
from .permissions import IsSuperuserPermissionOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserPermissionOrReadOnly] 
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


    def destroy(self, request, slug):
        instance = self.get_object(slug=self.kwargs.get('slug'))
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class GenreViewSet(viewsets.ModelViewSet):    
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsSuperuserPermissionOrReadOnly] 
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    

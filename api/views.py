from rest_framework import generics, viewsets, status, filters, permissions, viewsets, serializers
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import get_object_or_404
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Category, Title, Genre, GenreTitle
from .serializers import CategorySerializer, TitleSerializer, GenreSerializer
from .permissions import IsSuperuserPermissionOrReadOnly

User = get_user_model()

from .models import (
    Comment,
    Review,
    Title
)
from .serializers import (
    CommentSerializer,
    ReviewSerializer
)

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
    
    
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title_id=self.kwargs.get('title_id')
        )

        return review.comments.all()
    
    def perform_create(self, serializer):
        get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title_id=self.kwargs.get('title_id')
        )

        serializer.save(author=self.request.user)

        
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id')
        )

        return title.reviews.all()
    
    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            pk=self.kwargs.get('title_id')
        )

        if Review.objects.filter(
            author=self.request.user,
            title_id=title.id
            ).exists():

            serializer.save(
                author=self.request.user,
                title_id=title
            )
        raise serializers.ValidationError(
                {'errors': 'you already reviewed'}
            )
  
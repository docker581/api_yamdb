from rest_framework import generics, viewsets, status, filters, permissions, viewsets, serializers
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import get_object_or_404
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Category, Title, Genre, GenreTitle, Comment, Review
from .serializers import CategorySerializer, TitleSerializer, GenreSerializer, CommentSerializer, ReviewSerializer, Title2Serializer
from .permissions import IsSuperuserPermissionOrReadOnly, IsOwnerOrReadOnly

User = get_user_model()


class CategoryViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserPermissionOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsSuperuserPermissionOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre__slug', 'category__slug', 'year', ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializer
        return Title2Serializer

    def get_queryset(self):
        queryset = queryset = Title.objects.annotate(rating=Avg('reviews__score'))
        category = self.request.query_params.get('category', None)
        genre = self.request.query_params.get('genre', None)
        name = self.request.query_params.get('name', None)
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        if genre is not None:
            queryset = queryset.filter(genre__slug=genre)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class GenreViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsSuperuserPermissionOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly & IsAuthenticatedOrReadOnly, )

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

        serializer.save(author=self.request.user, review_id_id=self.kwargs.get('review_id'))


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly & IsAuthenticatedOrReadOnly, )

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
            raise serializers.ValidationError(
                {'errors': 'you already reviewed'}
            )

        serializer.save(
                author=self.request.user,
                title_id=title
            )

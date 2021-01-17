from django.contrib import auth
from rest_framework import viewsets, serializers
from rest_framework.generics import get_object_or_404
from django.contrib.auth import get_user_model


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

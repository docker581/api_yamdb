from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import 
from .views import (
    CategoryViewSet, 
    TitleViewSet, 
    GenreViewSet, 
    CommentViewSet,
    ReviewViewSet
)


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]

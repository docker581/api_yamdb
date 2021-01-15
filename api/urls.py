from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CurrentCategoryViewSet, TitleViewSet, CurrentTitleViewSet, GenreViewSet, CurrentGenreViewSet


router = DefaultRouter()
router.register('api/v1/categories', CategoryViewSet)
router.register('api/v1/categories/{slug}', CurrentCategoryViewSet)
router.register('api/v1/titles', TitleViewSet)
router.register('api/v1/titles/{titles_id}', CurrentTitleViewSet)
router.register('api/v1/genres', GenreViewSet)
router.register('api/v1/genres/{slug}', CurrentGenreViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

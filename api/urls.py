from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CurrentCategoryViewSet, TitleViewSet, CurrentTitleViewSet, GenreViewSet, CurrentGenreViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('categories/{slug}', CurrentCategoryViewSet)
router.register('titles', TitleViewSet)
router.register('titles/{titles_id}', CurrentTitleViewSet)
router.register('genres', GenreViewSet)
router.register('genres/{slug}', CurrentGenreViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenRefreshView

from . import views 

router = DefaultRouter()
router.register(r'v1/users', views.UserViewSet, basename='users') 
router.register(r'v1/users/me', views.UserMeViewSet, basename='users_me')

urlpatterns = router.urls
urlpatterns += [
    path('v1/auth/email/', views.EmailAPIView.as_view(), name='email'),
    path('v1/auth/token/', views.TokenView.as_view(), name='token'),
]

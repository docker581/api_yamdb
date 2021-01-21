from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views 

urlpatterns = [
    path('auth/email/', views.EmailAPIView.as_view(), name='email'),
    path('auth/token/', views.TokenView.as_view(), name='token'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
]

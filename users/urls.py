from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views 

urlpatterns = [
    path('v1/auth/email/', views.EmailAPIView.as_view(), name='email'),
    path('v1/auth/token/', views.TokenView.as_view(), name='token'),
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
]

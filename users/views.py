from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.decorators import permission_classes, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from rest_framework_simplejwt.views import TokenViewBase

from .serializers import UserSerializer, TokenSerializer
from .models import User
from .permissions import IsAdmin


class EmailAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        username = email.split('@')[0]
        user, created = User.objects.get_or_create(
            username=username,
            email=email,
            is_active=False,
        )
        confirmation_code = default_token_generator.make_token(user)
        user.confirmation_code = confirmation_code
        user.save()
        send_mail(
            f'User with email {email}',
            f'Your confirmation_code is {confirmation_code}',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return Response({'confirmation_code': confirmation_code})


class TokenView(TokenViewBase):
    serializer_class = TokenSerializer


@permission_classes([IsAuthenticated, IsAdmin])
class UserViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('search', None)
        if username is not None:
            user_id = User.objects.get(username=username).id
            queryset = queryset.filter(user=user_id)
        return queryset

    def perform_create(self, serializer):
        email = self.request.query_params.get('email', None)
        username = self.request.query_params.get('username', None)
        serializer.save(email=email, username=username)


@permission_classes([IsAuthenticated, IsAdmin])
class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'username'

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('search', None)
        if username is not None:
            user_id = User.objects.get(username=username).id
            queryset = queryset.filter(user=user_id)
        return queryset

    # def perform_create(self, serializer):
    #     email = self.request.query_params.get('email', None)
    #     serializer.save(email=email)

    def retrieve(self, pk, username):
        user = User.objects.get(username=username)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(methods=['get', 'patch'], detail=False,
            permission_classes=[IsAuthenticated],
            url_path='me', url_name='personal_data')
    def personal_data(self, request):
        user = User.objects.get(username=request.user.username)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

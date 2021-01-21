from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenViewBase

from .serializers import UserSerializer, TokenSerializer
from .models import User


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

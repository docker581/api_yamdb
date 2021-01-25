
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    CHOICES = ((USER, 'user'), (MODERATOR, 'moderator'), (ADMIN, 'admin'))

    email = models.EmailField(unique=True, db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    role = models.TextField(
        choices=CHOICES,
        default=USER,
    )
    username = models.CharField(unique=True, max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    confirmation_code = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.is_active = True
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['email']

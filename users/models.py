from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    USER = 'user', 'user'
    MODERATOR = 'moderator', 'moderator'
    ADMIN = 'admin', 'admin'
    CHOICES = (USER, MODERATOR, ADMIN)

    email = models.EmailField(unique=True, db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    role = models.TextField(
        choices=CHOICES,
        default=USER, 
    )
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

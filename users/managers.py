from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username=None):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password, username)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'admin'
        user.save()
        return user
        
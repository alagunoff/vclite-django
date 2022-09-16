from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, username: str, first_name: str, password: None = None) -> 'User':
        user: User = self.model(
            username=username,
            first_name=first_name
        )
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username: str, first_name: str, password: None = None) -> 'User':
        user = self.create_user(
            username,
            first_name,
            password,
        )
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='images/users', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()
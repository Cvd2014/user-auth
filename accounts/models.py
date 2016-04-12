from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


# Create your models here.
class AccountUserManager(UserManager):
    def create_user(self, username, email, password, is_staff, is_superuser, **extrafields):
        """
        Creates and saves a User with the given username, email and password
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now, **extrafields
                          )
        user.set_password = (password)
        user.save(using=self.db)
        return user


class User(AbstractUser):
    stripe_id = models.CharField(max_length=40, default='')
    subscription_end=models.DateTimeField(default=timezone.now)
    objects = AccountUserManager()
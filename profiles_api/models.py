from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ User Profile Manager """

    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('Usuario debe tener un Email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database Model for Users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Get full name of the user """
        return self.name

    def get_short_name(self):
        """ Get short name of the user"""
        return self.name

    def __str__(self) -> str:
        """ Return string representing the user """
        return self.email

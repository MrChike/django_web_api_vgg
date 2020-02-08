from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UsersProfileManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsersProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.get_email_field_name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email


class Projects(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    is_complete = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Actions(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    description = models.TextField()
    note = models.TextField()

    def __str__(self):
        return self.description

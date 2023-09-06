from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import models as authmodel


class User(AbstractUser):
    bio = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.username

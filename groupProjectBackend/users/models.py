from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)
    credentials = models.TextField()

    def __str__(self):
        return self.username

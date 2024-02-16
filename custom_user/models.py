from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
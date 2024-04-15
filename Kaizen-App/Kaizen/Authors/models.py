from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self) -> str:
        return super().__str__()

      
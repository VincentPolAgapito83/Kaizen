from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    articles = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
from django.db import models
from django.contrib.auth.models import User


class Authors(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    school = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
    
class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    authors = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    date_published = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return super().__str__()
    
class Kaizenuser(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self) -> str:
        return super().__str__()

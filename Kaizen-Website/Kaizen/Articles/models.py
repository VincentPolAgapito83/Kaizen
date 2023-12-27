from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)

    def _str_(self):
        return self.title()

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username

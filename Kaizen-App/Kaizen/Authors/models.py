from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=200)
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title()

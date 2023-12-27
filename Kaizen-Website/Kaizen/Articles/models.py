from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)

    def _str_(self):
        return self.title()

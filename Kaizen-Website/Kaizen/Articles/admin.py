from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from .models import Articles

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "authors",)

admin.site.register(Articles, ArticlesAdmin)



# Register User and profile

from django.contrib import admin
from .models import Authors

# Register your models here.

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department", "articles" )

admin.site.register(Authors)


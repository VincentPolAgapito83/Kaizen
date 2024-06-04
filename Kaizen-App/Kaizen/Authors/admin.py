from django.contrib import admin
from .models import UserProfile


class UserProfile(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


admin.site.register(UserProfile)






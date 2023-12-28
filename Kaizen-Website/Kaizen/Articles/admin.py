from django.contrib import admin
from .models import Articles

# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "authors",)

class Profile(admin.ModelAdmin):
    list_display = ("user", "image", "name", "email", "department" )

admin.site.register(Articles, ArticlesAdmin)



# Register User and profile

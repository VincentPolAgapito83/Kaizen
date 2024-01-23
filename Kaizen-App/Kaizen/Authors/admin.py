from django.contrib import admin
from .models import Authors, Article, Kaizenuser

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department", "school" )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "authors","department", "date published")

class KaizenuserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


admin.site.register(Authors)
admin.site.register(Article)
admin.site.register(Kaizenuser)


from django.contrib import admin
from .models import Article

admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publication_date', 'publisher')







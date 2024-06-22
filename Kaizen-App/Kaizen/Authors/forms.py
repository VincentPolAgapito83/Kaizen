from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'authors', 'publication_date', 'publisher', 'uploaded_file']

class SearchForm(forms.Form):
    person_to_search = forms.CharField(label='Person to Search', max_length=100)




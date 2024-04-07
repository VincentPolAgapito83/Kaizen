from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Authors

class AuthorsForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'

class SearchForm(forms.Form):
    person_to_search = forms.CharField(label='Person to Search', max_length=100)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
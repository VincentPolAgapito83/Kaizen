from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name' ,'email']

class SearchForm(forms.Form):
    person_to_search = forms.CharField(label='Person to Search', max_length=100)


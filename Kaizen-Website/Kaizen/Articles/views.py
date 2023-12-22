from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Articles
from django.db.models import Q

def search_bar(request):
    if request.method == "POST":
        results = request.POST['results']
        return render(request, 'searchbar.html',
                       {'results':results}) 
    else:
        return render(request, 'searchbar.html', {})

def user_registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Account Created Successfully')
            
    context = {'form':form}
    return render(request, 'members/registration2.html', context)

def user_login(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, email)

    context = {}
    return render(request, 'members/login2.html', context)


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Articles
    template_name = 'search_results.html'

    def get_queryset(self):
        return Articles.objects.filter(
            Q(authors__icontains="") | Q(title__icontains="")
        )


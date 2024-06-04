from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import json
from serpapi import GoogleSearch
from .forms import UserProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models import Q
from serpapi import GoogleSearch
from .forms import SearchForm # Import your search form

def index(request):
    User=UserProfile.objects.all()
    return render(request,'index.html',{'user': User})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['email']
    User=UserProfile(firstname=x,lastname=y,email=z)
    User.save()
    return redirect("/")

def delete(request,id):
    User=User.objects.get(id=id)
    User.delete()
    return redirect("/")

def update(request,id):
    User=User.objects.get(id=id)
    return render(request,'update.html',{'User':User})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['email']
    User=User.objects.get(id=id)
    User.firstname=x
    User.lastname=y
    User.country=z
    User.save()
    return redirect("/")

def search_form(request):
       if request.method == "POST":
        searched = request.POST('searched')
        return render(request, 'searchform.html', {'searched':searched})
       else:
        return render(request, 'searchform.html', {})

    
def user_logout(request):
    logout(request)
    messages.success(request, ("Logout Successfully"))
    return redirect('login')

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Account Created Successfully')
            return redirect('home.html')
        else:
            form = UserProfileForm()


    return render(request, 'register.html')


def user_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           user = form.get_user()
           login(request, user)
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html')
    
class userprofile(View):
  template_name = 'profile/profile.html'

  def get(self, request, author_id):

        params = {
          "api_key": "425d6fb5ad378e6887055b328dad42d7ff166d2476aaefd7b2c6a814312ed22f",
          "author_id": author_id,
          "engine": "google_scholar_author",
          "hl": "en",
        
        }

        search = GoogleSearch(params) # Assuming GoogleSearch is your model to interact with the API
        results = search.get_dict()
        author = results.get("author", {})
        articles = results.get("articles", [{}])
        
        return render (request, self.template_name, {'author': author, 'articles': articles})
    
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchForm(self.request.GET or None)  # Initialize the form with GET data if present

        profiles = []
        if self.request.method == 'GET' and form.is_valid():
            person_to_search = form.cleaned_data.get('person_to_search')
            params = {
                "api_key": "425d6fb5ad378e6887055b328dad42d7ff166d2476aaefd7b2c6a814312ed22f",
                "engine": "google_scholar_profiles",
                "hl": "en",
                "mauthors": person_to_search,
            }
            search = GoogleSearch(params)
            results = search.get_dict()
            profiles = results.get("profiles", [])

        context['form'] = form
        context['profiles'] = profiles
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SearchProfileView(View):
    template_name = 'search_profile.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(request.GET)  # Bind request.GET data to the form
        profiles = []

        if form.is_valid():
            person_to_search = form.cleaned_data.get('person_to_search')
            params = {
                "api_key": "5d2bc0b24f17c12c1fda9195a38221181057d1c980d264547a3d99fb90a8c392",
                "engine": "google_scholar_profiles",
                "hl": "en",
                "mauthors": person_to_search  # Update with the value from the form
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            profiles = results.get("profiles", [])

        return render(request, self.template_name, {'profiles': profiles, 'form': form})
    
              
           



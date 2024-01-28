from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import json
from serpapi import GoogleSearch
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView, ListView, View
from .models import Authors
from django.db.models import Q
 
def search_form(request):
    if request.method == "POST":
        searched = request.POST('searched')
        return render(request, 'searchform.html', {'searched':searched})
    else:
        return render(request, 'searchform.html', {})


def user_profile(request):
    
    if request.method == "POST":
        results = request.POST['results']
        user_profile = request.POST['profile']
        response_data = {'status':'success'}
      
    return render(request, 'members/profile.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, ("Logout Successfully"))
    return redirect('login')

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
    
class Displayprofileview(View):
    template_name = 'profiles/profile.html'

    def get(self, request, *args, **kwargs):

        params = {
          "api_key": "5d2bc0b24f17c12c1fda9195a38221181057d1c980d264547a3d99fb90a8c392",
          "engine": "google_scholar_profiles",
          "hl": "en",
          "mauthors": '"Verlyn Nojor" OR "Menchie Miranda"'
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        profiles = results["profiles"]

        return render (request, self.template_name, {'profiles': profiles})
    
class Profile(View):
    template_name = 'profiles/profile2.html'

    def get(self, request, *args, **kwargs):

       
      params = {
      "api_key": "5d2bc0b24f17c12c1fda9195a38221181057d1c980d264547a3d99fb90a8c392",
      "engine": "google_scholar_profiles",
      "hl": "en",
      "mauthors": "Jonathan V.Taylar"
    }

      search = GoogleSearch(params)
      results = search.get_dict()
      profile = results["profile"]


      return render (request, self.template_name, {'profile': profile})
    
class Display(View):
    template_name = 'profiles/profile3.html'

    def get(self, request, *args, **kwargs):

       params = {
      "api_key": "5d2bc0b24f17c12c1fda9195a38221181057d1c980d264547a3d99fb90a8c392",
      "engine": "google_scholar_profiles",
      "hl": "en",
      "mauthors": "ryan francisco tip"
    }

       search = GoogleSearch(params)
       results = search.get_dict()
       profile = results["profile"]
    
       return render (request, self.template_name, {'profile': profile})
 
class ProfileView(View):
    template_name = 'profiles/profile4.html'

    def get(self, request, *args, **kwargs):

       
      params = {
      "api_key": "5d2bc0b24f17c12c1fda9195a38221181057d1c980d264547a3d99fb90a8c392",
      "engine": "google_scholar_profiles",
      "hl": "en",
      "mauthors": "Roman M. richard"
    }

      search = GoogleSearch(params)
      results = search.get_dict()
      profile = results["profile"]
    
      return render (request, self.template_name, {'profile': profile})
    
class DisplayView(View):
    template_name = 'profiles/profile5.html'

    def get(self, request, *args, **kwargs):

       
      params = {
     "api_key": "5d2bc0b24f17c12c1fda9195a38221181057d1c980d264547a3d99fb90a8c392",
     "engine": "google_scholar_profiles",
     "hl": "en",
     "mauthors": "alonica villanueva"
}

      search = GoogleSearch(params)
      results = search.get_dict()
      profile = results["profile"]
    
      return render (request, self.template_name, {'profile': profile})

class DisplayProfile(View):
    template_name = 'profiles/profile6.html'

    def get(self, request, *args, **kwargs):

       
      params = {
     "api_key": "5d2bc0b24f17c12c1fda9195a38221181057d1c980d264547a3d99fb90a8c392",
     "engine": "google_scholar_profiles",
     "hl": "en",
     "mauthors": "Verlyn Nojor"
}

      search = GoogleSearch(params)
      results = search.get_dict()
      profile = results["profile"]
    
      return render (request, self.template_name, {'profile': profile})
    
class informationview(TemplateView):
    template_name = 'information.html'

class uploadview(TemplateView):
    template_name = 'upload.html'
    
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class SearchResultsView(ListView):
    model = Authors
    template_name = 'search_results.html'

    def SearchResultsView(self):
        return Authors.object.filter()
    












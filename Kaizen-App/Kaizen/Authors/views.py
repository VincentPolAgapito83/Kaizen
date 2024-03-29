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
from django.contrib.auth.models import User
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


class information(TemplateView):
    template_name = 'information.html'

class upload(TemplateView):
    template_name = 'upload.html'
    
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class SearchResultsView(ListView):
    model = Authors
    template_name = "search_results.html"

    def search(request):  # new
        if request.method == 'GET':
        
            search_query = request.GET.get('Authors', None)
            print(search_query)
            Authors_list_obj = Authors.objects.filter(Authors__icontains=search_query)

            if (len(Authors_list_obj)) > 0:
                print("Authors Found")
                return render(request, 'search_results.html', {'Authors_list_obj': Authors_list_obj,})
            else:
                print("Authors Not Found")
              
        return render(request, 'search_results.html', {})
    
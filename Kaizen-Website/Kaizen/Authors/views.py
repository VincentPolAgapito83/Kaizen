from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Authors
from django.db.models import Q
from scholarly import scholarly



def search_form(request):
    if request.method == "POST":
        searched = request.POST('searched')

        return render(request, 'searchform.html', {'searched':searched})
    else:
        return render(request, 'searchform.html', {})


def user_profile(request):
    API_KEY = open("API_KEY", "r").read()
    user_profile_url = "https://serpapi.com/search?engine=google_scholar_profiles"

    if request.method == "POST":
        results = request.POST['results']
        user_profile = request.POST['profile']
        response_data = {'status':'success'}
      
    return render(request, 'members/profile.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, ("Logout Successfully"))
    return redirect('home')

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

def search_results(request):

    if request.method == 'POST':
      Authors_url = 'https://serpapi.com/search?engine=google_scholar_profiles'
   
    search_params = {
       'Authors' : 'name',
       'Authors' : 'email',
       'Authors' : 'department',
       'Authors' : 'articles',
       'q' : request.POST['search']

    }

    r = requests.get(Authors_url, params=search_params)
    results = scholarly.json()
   
    if len(results):
       for result in results:
           articles_data = {
           'Title' : result['title'],
           'Published_date': result['published_date'],
           'Co-Author' : result['co-author'],
           'Description' : result['description']
       }

       Authors.append(Authors_data)  

    else:
      message = print('No results found')

    context = {
      'Authors' : Authors

}
    return render(request, 'search_results.html', context)


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SearchResultsView(ListView):
    model = Authors
    template_name = 'search_results.html'

    def get_queryset(self):
        return Authors.objects.filter( )
        



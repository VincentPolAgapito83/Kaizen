from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from .models import Articles
from django.db.models import Q


def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            
    context = {'form':form}
    return render(request, 'members/registration.html', context)



class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Articles
    template_name = 'search_results.html'

    def get_queryset(self):
        return Articles.objects.filter(
            Q(authors__icontains="") | Q(title__icontains="")
        )


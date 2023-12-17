from django.urls import path
from . import views
from .views  import HomePageView, SearchResultsView

urlpatterns = [
    path('register/', views.registration, name="register"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('', HomePageView.as_view(), name="home"),
]
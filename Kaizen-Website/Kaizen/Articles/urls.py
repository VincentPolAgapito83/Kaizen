from django.urls import path
from . import views
from .views  import HomePageView, SearchResultsView

urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('login/', views.user_login, name="login"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('search/', views.search_bar, name="search-bar"),
    path('', HomePageView.as_view(), name="home"),
]
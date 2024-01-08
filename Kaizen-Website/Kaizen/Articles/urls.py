from django.urls import path
from . import views
from .views  import HomePageView, SearchResultsView

urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.user_profile, name="profile"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('searchform/', views.search_form, name="search_form"),
    path('', HomePageView.as_view(), name="home"),
]
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomePageView, SearchResultsView, AboutPageView, informationview, uploadview, Displayprofileview, Profile,Display, ProfileView, DisplayView, DisplayProfile
from django.contrib import admin

urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profiles/', Displayprofileview.as_view(), name="profiles"),
    path('profiles/', Profile.as_view(), name="profiles"),
    path('profiles/', ProfileView.as_view(), name="profiles"),
    path('profiles/', Display.as_view(), name="profiles"),
    path('profiles/', DisplayView.as_view(), name="profiles"),
    path('profiles/', DisplayProfile.as_view(), name="profiles"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('searchform/', views.search_form, name="search_form"),
    path('information/', informationview.as_view(), name="information"),
    path ('upload/', uploadview.as_view(), name="upload"),
    path('', HomePageView.as_view(), name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
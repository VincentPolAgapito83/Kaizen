from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomePageView, SearchResultsView, AboutPageView, Displayprofileview, information, upload
from django.contrib import admin

urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profiles/', Displayprofileview.as_view(), name="profiles"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('searchform/', views.search_form, name="search_form"),
    path('information/', information.as_view(), name="information"),
    path ('upload/', upload.as_view(), name="upload"),
    path('', HomePageView.as_view(), name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
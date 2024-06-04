from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import HomePageView, SearchProfileView, AboutPageView, userprofile
from django.contrib import admin

urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('profile/<str:author_id>/', userprofile.as_view(), name="profile"),
    path('search/', SearchProfileView.as_view(), name="search_profile"),
    path('searchform/', views.search_form, name="search_form"),
    path('', HomePageView.as_view(), name="home"),
     path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec")
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
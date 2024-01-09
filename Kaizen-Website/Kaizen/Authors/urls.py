from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views  import HomePageView, SearchResultsView, AboutPageView

urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.user_profile, name="profile"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('searchform/', views.search_form, name="search_form"),
    path('', HomePageView.as_view(), name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
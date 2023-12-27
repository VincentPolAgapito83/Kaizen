from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views  import HomePageView, SearchResultsView

urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.user_profile, name="profile"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('search/', views.search_bar, name="search-bar"),
    path('', HomePageView.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
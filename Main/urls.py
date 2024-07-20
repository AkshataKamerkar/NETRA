from django.urls import path
from .views import LandingPage, AboutUs, Dashboard
from . import views

app_name = 'main'

urlpatterns = [
    path('',LandingPage.as_view(),name='index'),
    path('about',AboutUs.as_view(),name='about'),
    path('dashboard',Dashboard.as_view(),name='dashboard'),
    
]
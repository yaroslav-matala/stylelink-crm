from . import views
from django.urls import path

urlpatterns = [
    path('home-alt/', views.HomePage.as_view(), name='home_alt'),
    path('', views.home, name='home')
]
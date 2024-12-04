from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('add-client', views.add_client, name='add-client')
]
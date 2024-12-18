from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('add-client', views.add_client, name='add-client'),
    path('update-client/<int:pk>/', views.update_client, name='update-client'),
    path('client/<int:pk>', views.singular_client, name='client'),
    path('delete-client/<int:pk>', views.delete_client, name="delete-client"),
    path('switch-theme/', views.switch_theme, name='switch_theme'),
]

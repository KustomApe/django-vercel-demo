import django.contrib.auth.views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/<int:vehicle_id>', views.vehicle, name='vehicle'),
    path('search_vehicles', views.search_vehicles, name='search_vehicles'),
]

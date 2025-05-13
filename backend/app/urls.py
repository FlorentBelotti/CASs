from django.urls import path
from . import views

urlpatterns = [

    # Default path
    path('', views.home, name='home'),
    
    # Alternative home path
    path('home/', views.home, name='home-alt'),

    # Debug API path
    path('api/test/', views.vanilla_view, name='api-test'),
]
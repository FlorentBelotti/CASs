from django.urls import path
from . import views

urlpatterns = [

    # Default path
    path('', views.home, name='home'),
    
    # Debug API path
    path('api/test/', views.vanilla_view, name='api-test'),
]
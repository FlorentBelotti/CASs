from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Session, Exercise, Serie

# Render view

def home(request):
    recent_sessions = Session.objects.all().order_by('-date')[:5]
    return render(request, 'home.html', {
        'recent_sessions': recent_sessions
    })

# API views
@api_view(['GET'])
def vanilla_view(request):
    return Response({"CASs: Debug": "Vanilla response"})
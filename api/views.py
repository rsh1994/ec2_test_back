# backend/api/views.py

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

# React 앱을 서빙하는 view
index = never_cache(TemplateView.as_view(template_name='index.html'))

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Welcome to the API!"})

@api_view(['GET'])
def get_data(request):
    data = {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ]
    }
    return Response(data)
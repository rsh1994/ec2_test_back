from django.urls import path
from .views import api_home, get_data

urlpatterns = [
    path('', api_home, name='api_home'),
    path('data/', get_data, name='get_data'),
]
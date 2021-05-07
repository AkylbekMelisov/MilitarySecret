from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterView.as_view(), name='create'),
    path('cars/', CarView.as_view())
]

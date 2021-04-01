from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterView.as_view()),
    path('cars/', CarView.as_view())
]

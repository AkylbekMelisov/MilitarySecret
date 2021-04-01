from django.urls import path
from .views import *

urlpatterns = [
    path('documents/', DocumentView.as_view()),
]

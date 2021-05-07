from django.shortcuts import render
from rest_framework import views, viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class RegisterView(views.APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CarView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            cars = Car.objects.all()
        else:
            cars = Car.objects.filter(dossier=request.user.dossier)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

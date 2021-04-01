from django.core.mail import EmailMessage
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_model', 'year', 'country', 'color', 'mark', 'wheel_type', 'car_type', 'car_number']


class DossierSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Dossier
        fields = ['id', 'image', 'full_name', 'address', 'department', 'date_birth',
                  'phone', 'experience', 'cars'
                  ]


class RegisterSerializer(serializers.ModelSerializer):
    dossier = DossierSerializer()
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'dossier']

    def create(self, validated_data):
        dossier = validated_data.pop('dossier')
        cars_data = dossier.pop('cars')
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if confirm_password == password:
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.is_active = False
            user.save()
            subject = 'New user'
            body = f"New user with username: {user.username} and selected department: {dossier['department']}"
            to_list = []
            super_list = User.objects.filter(is_superuser=True)
            for super in super_list:
                to_list.append(super.email)
            # email = EmailMessage(subject=subject, body=body, to=to_list)
            # email.send()
            dossier_data = Dossier.objects.create(user=user, **dossier)
            print(cars_data)
            for car in cars_data:
                Car.objects.create(dossier=dossier_data, **car)
            return user
        else:
            raise ValidationError("Passwords dont match!")

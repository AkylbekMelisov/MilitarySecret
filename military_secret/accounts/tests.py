from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
class RegisterTestCase(APITestCase):
    def setUp(self):
        self.my_url = reverse('create')
    def test_user_create(self):
        data = {
                    "username": "maksim",
                    "email": "maximneveraa@gmail.com",
                    "password": "123456",
                    "confirm_password":"123456",
                    "dossier": {
                        "id": 1,
                        "full_name": "Суровкин Максим",
                        "address": "Lalaland",
                        "department": "SpF",
                        "date_birth": "1998-07-26",
                        "phone": "+996555506006",
                        "experience": 2,
                        "cars": [
                            {
                                "id": 1,
                                "car_model": "fit",
                                "year": 2000,
                                "mark": "honda",
                                "color": "black",
                                "country": "korea",
                                "car_number": "D001R",
                                "car_type": "service",
                                "wheel_type": "RH"
                            }
                        ]
                    }
                }
        self.post_data = self.client.post(self.my_url,data,format='json')
        self.assertEqual(self.post_data.status_code,status.HTTP_201_CREATED)

    def test_password_dont_match(self):
        data = {
            "username": "maksim",
            "email": "maximneveraaasdvasdvasdasdas12312",
            "password": "123456",
            "confirm_password": "asdasdasdasdas",
            "dossier": {
                "id": 1,
                "full_name": "Суровкин Максим",
                "address": "Lalaland",
                "department": "SpF",
                "date_birth": "1998-07-26",
                "phone": "+996555506006",
                "experience": 2,
                "cars": [
                    {
                        "id": 1,
                        "car_model": "fit",
                        "year": 2000,
                        "mark": "honda",
                        "color": "black",
                        "country": "korea",
                        "car_number": "D001R",
                        "car_type": "service",
                        "wheel_type": "RH"
                    }
                ]
            }
        }
        self.post_data = self.client.post(self.my_url,data,format='json')
        self.assertEqual(self.post_data.status_code,status.HTTP_400_BAD_REQUEST)
#date_birth , email , phone , full_name
    def test_create_without_cars(self):
        data = {
            "username": "maksim",
            "email": "akylbek.melisov@gmail.com",
            "password": "123456",
            "confirm_password": "123456",
            "dossier": {
                "id": 1,
                "full_name": "Суровкин Максим",
                "address": "Lalaland",
                "department": "SpF",
                "date_birth": "1998-07-26",
                "phone": "+996555506006",
                "experience": 2,
                "cars": []
            }
        }
        self.post_data = self.client.post(self.my_url, data, format='json')
        self.assertEqual(self.post_data.status_code,status.HTTP_201_CREATED)

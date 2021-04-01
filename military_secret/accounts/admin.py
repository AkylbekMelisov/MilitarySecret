from django.contrib import admin
from .models import *

admin.site.register(Dossier)


class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'year', 'country', 'color', 'mark', 'car_number']


admin.site.register(Car, CarAdmin)

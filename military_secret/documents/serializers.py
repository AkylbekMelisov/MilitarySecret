from rest_framework import serializers
from .models import Document
from django.utils import timezone
from .services import count_time


class DocumentSerializer(serializers.ModelSerializer):
    expired_method = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = '__all__'

    def get_expired_method(self, obj):
        date = obj.date_created
        current_time = timezone.now()
        difference = count_time(date, current_time)
        if abs(difference) > (obj.date_expired * 60):
            obj.status = 'dead'
            obj.save()
        return 1

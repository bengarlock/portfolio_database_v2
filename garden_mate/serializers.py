from rest_framework import serializers
from .models import Day


class GardenDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

from rest_framework import serializers
from .models import ResyRestaurant, ResyTotalCount


class ResyRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyRestaurant
        fields = '__all__'


class ResyTotalCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyTotalCount
        fields = '__all__'

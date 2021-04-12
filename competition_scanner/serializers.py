from rest_framework import serializers
from .models import ResyRestaurant, ResyTotalCount, YelpRestaurant, YelpTotals


class ResyRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyRestaurant
        fields = '__all__'


class ResyTotalCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyTotalCount
        fields = '__all__'


class YelpRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpRestaurant
        fields = '__all__'


class YelpTotalCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpTotals
        fields = '__all__'

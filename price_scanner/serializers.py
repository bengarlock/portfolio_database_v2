from rest_framework import serializers
from .models import Price, Favorite


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Favorite
        fields = '__all__'

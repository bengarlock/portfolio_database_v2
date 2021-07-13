from rest_framework import serializers
from .models import Price, Favorite


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, required=False)

    class Meta:
        model = Favorite
        fields = ['id', 'name', 'url', 'image', 'created_at', 'updated_at', 'prices']
        depth = 2

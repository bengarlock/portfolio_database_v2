from rest_framework import serializers
from .models import PriceUrls

class PriceUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceUrls
        fields = '__all__'
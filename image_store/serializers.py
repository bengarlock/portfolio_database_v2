from rest_framework import serializers
from .models import ImageStore


class ImageStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageStore
        fields = '__all__'

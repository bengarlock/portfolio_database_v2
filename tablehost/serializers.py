from rest_framework import serializers
from .models import Book, Guest, Slot, Restaurant, Table


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'



class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(many=True, required=False)
    slots = SlotSerializer(many=True, required=False)
    class Meta:
        model = Book
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

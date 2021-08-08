from rest_framework import serializers
from .models import Book, Guest, Slot, Restaurant, Table


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(required=False)

    class Meta:
        model = Slot
        fields = ['id', 'booked', 'time', 'party_size', 'status', 'reservation_notes', 'tables', 'created_at',
                  'updated_at', 'book', 'guest']

    depth = 1


class BookSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = ['id', 'date', 'restaurant_id', 'created_at', 'updated_at', 'slots']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

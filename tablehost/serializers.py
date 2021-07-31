from rest_framework import serializers
from .models import Book, Guest, Slot, Restaurant, Table


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'booked', 'time', 'party_size', 'status', 'reservation_notes', 'tables', 'guest', 'book']
        depth = 1

class SlotSerializerNoBookView(serializers.ModelSerializer):
    #excludes book view so book endpoint does not render redunant data.
    class Meta:
        model = Slot
        fields = ['id', 'booked', 'time', 'party_size', 'status', 'reservation_notes', 'tables', 'guest']
        depth = 1


class BookSerializer(serializers.ModelSerializer):
    slots = SlotSerializerNoBookView(many=True, required=False)
    class Meta:
        model = Book
        fields = '__all__'
        depth = 2


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

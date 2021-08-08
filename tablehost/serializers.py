from rest_framework import serializers
from .models import Book, Guest, Slot, Restaurant, Table, Status


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(required=False)


    class Meta:
        model = Slot
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.booked = validated_data.get('booked', instance.booked)
    #     instance.time = validated_data.get('time', instance.time)
    #     instance.party_size = validated_data.get('party_size', instance.party_size)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.reservation_notes = validated_data.get('reservation_notes', instance.reservation_notes)
    #     instance.tables = validated_data.get('tables', instance.tables)
    #     instance.book = validated_data.get('book', instance.book)
    #     instance.save()
    #
    #     if validated_data.pop('guest'):
    #         guest_data = validated_data.pop("guest")
    #         guest = instance.guest
    #         guest.first_name = guest_data.get('first_name', guest.first_name)
    #         guest.last_name = guest_data.get('last_name', guest.last_name)
    #         guest.phone_number = guest_data.get('phone_number', guest.phone_number)
    #         guest.guest_notes = guest_data.get('guest_notes', guest.guest_notes)
    #         guest.active = guest_data.get('active', guest.active)
    #         guest.id = guest_data.get('id', guest.id)
    #         guest.save()
    #
    #     return instance




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


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

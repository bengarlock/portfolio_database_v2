from rest_framework import serializers
from .models import Book, Guest, Slot, Restaurant, Table


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'guest_notes', 'root_user', 'slots']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'booked', 'time', 'party_size', 'status', 'reservation_notes', 'tables', 'book', 'guest']

    def create(self, validated_data):
        Slot.objects.create(**validated_data)
        return Slot(**validated_data)

    def update(self, instance, validated_data):
        instance.booked = validated_data.get('booked', instance.booked)
        instance.time = validated_data.get('time', instance.time)
        instance.party_size = validated_data.get('party_size', instance.party_size)
        instance.status = validated_data.get('status', instance.status)
        instance.reservation_notes = validated_data.get('reservation_notes', instance.reservation_notes)
        instance.tables = validated_data.get('tables', instance.tables)
        instance.guest = validated_data.get('guest', instance.guest)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, required=False)

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

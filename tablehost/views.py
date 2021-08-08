from rest_framework import viewsets, filters, generics
from .models import Book, Slot, Restaurant, Guest, Table
from .serializers import BookSerializer, SlotSerializer, RestaurantSerializer, GuestSerializer, TableSerializer
import django_filters.rest_framework
from rest_framework.pagination import PageNumberPagination


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['date']


class SlotView(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class GuestView(generics.ListAPIView):
    # queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name", "phone_number", "active", ]
    ordering_fields = ['last_name', 'phone_number']
    ordering = ['last_name']

    def get_queryset(self):
        queryset = Guest.objects.all()
        return queryset



class TableView(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

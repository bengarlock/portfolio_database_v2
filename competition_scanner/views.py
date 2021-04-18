from .models import ResyRestaurant, ResyTotalCount, YelpRestaurant, YelpTotals
from rest_framework import viewsets, permissions
from .serializers import ResyRestaurantSerializer, ResyTotalCountSerializer, YelpRestaurantSerializer, \
    YelpTotalCountSerializer
import django_filters.rest_framework


class ResyRestaurantViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = ResyRestaurant.objects.all()
    serializer_class = ResyRestaurantSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['resy_id']


class ResyTotalCountViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = ResyTotalCount.objects.all()
    serializer_class = ResyTotalCountSerializer


class YelpRestaurantViewSet(viewsets.ModelViewSet):
    queryset = YelpRestaurant.objects.all()
    serializer_class = YelpRestaurantSerializer


class YelpTotalCountViewSet(viewsets.ModelViewSet):
    queryset = YelpTotals.objects.all()
    serializer_class = YelpTotalCountSerializer

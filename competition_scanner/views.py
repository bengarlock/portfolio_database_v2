from .models import ResyRestaurant, ResyTotalCount, YelpRestaurant, YelpTotals
from rest_framework import viewsets, permissions
from .serializers import ResyRestaurantSerializer, ResyTotalCountSerializer, YelpRestaurantSerializer, \
    YelpTotalCountSerializer


class ResyRestaurantViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = ResyRestaurant.objects.all()
    serializer_class = ResyRestaurantSerializer


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

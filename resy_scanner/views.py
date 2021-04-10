from .models import ResyRestaurant, ResyTotalCount
from rest_framework import viewsets, permissions
from .serializers import ResyRestaurantSerializer, ResyTotalCountSerializer


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

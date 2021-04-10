from .models import ResyRestaurant, ResyTotalCount
from rest_framework import viewsets, permissions, serializers


class ResyRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyRestaurant
        fields = '__all__'


class ResyTotalCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyTotalCount
        fields = '__all__'


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

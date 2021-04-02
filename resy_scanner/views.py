from .models import ResyRestaurant
from rest_framework import viewsets, permissions, serializers


class ResySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyRestaurant
        fields = '__all__'


class ResyViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = ResyRestaurant.objects.all()
    serializer_class = ResySerializer

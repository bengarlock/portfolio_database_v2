from rest_framework import viewsets, permissions
from .serializers import PlayerSerializer
from .models import Player
import django_filters.rest_framework


# Create your views here.
class PlayerViewset(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ["player"]

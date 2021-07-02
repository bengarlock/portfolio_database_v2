from .models import Day
from rest_framework import viewsets
from .serializers import GardenDaySerializer


# Create your views here.
class GardenDayViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = Day.objects.all()
    serializer_class = GardenDaySerializer

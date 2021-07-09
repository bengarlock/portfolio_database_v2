from rest_framework import viewsets, permissions
from .serializers import PriceUrlsSerializer
from .models import PriceUrls
import django_filters.rest_framework


# Create your views here.
class PriceUrlVewSet(viewsets.ModelViewSet):
    queryset = PriceUrls.objects.all()
    serializer_class = PriceUrlsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["url"]

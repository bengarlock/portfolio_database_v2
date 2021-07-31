from django.shortcuts import render
from .models import ImageStore
from rest_framework import viewsets, permissions
from .serializers import ImageStoreSerializer
import django_filters.rest_framework


# Create your views here.
class ImageStoreViewset(viewsets.ModelViewSet):
    queryset = ImageStore.objects.all()
    serializer_class = ImageStoreSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ["image"]

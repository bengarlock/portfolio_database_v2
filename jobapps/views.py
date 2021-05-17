from .models import Jobapp
from rest_framework import viewsets, permissions, serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobapp
        fields = '__all__'


class JobappViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    queryset = Jobapp.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.jobapps.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

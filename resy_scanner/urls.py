from rest_framework import routers
from .views import ResyViewSet


router = routers.DefaultRouter()
router.register('api/v1/resy', ResyViewSet, 'resy')

urlpatterns = router.urls
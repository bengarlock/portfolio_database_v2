from rest_framework import routers
from .views import GardenDayViewSet

router = routers.DefaultRouter()
router.register('v1/garden/days', GardenDayViewSet, 'days')

urlpatterns = router.urls
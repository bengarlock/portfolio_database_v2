from rest_framework import routers
from .views import PlayerViewset

router = routers.DefaultRouter()
router.register('api/v1/healthtracker/players', PlayerViewset, 'players')

urlpatterns = router.urls
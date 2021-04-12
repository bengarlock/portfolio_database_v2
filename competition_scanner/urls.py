from rest_framework import routers
from .views import ResyRestaurantViewSet, ResyTotalCountViewSet


router = routers.DefaultRouter()
router.register('api/v1/resy/restaurants', ResyRestaurantViewSet, 'restaurants')
router.register('api/v1/resy/totals', ResyTotalCountViewSet, 'totals')

urlpatterns = router.urls
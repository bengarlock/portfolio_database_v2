from rest_framework import routers
from .views import ResyRestaurantViewSet, ResyTotalCountViewSet, ResyCollectionViewSet


router = routers.DefaultRouter()
router.register('api/v1/resy/restaurants', ResyRestaurantViewSet, 'restaurants')
router.register('api/v1/resy/totals', ResyTotalCountViewSet, 'totals')
router.register('api/v1/resy/collections', ResyCollectionViewSet, 'collections')

urlpatterns = router.urls
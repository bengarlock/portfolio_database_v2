from rest_framework import routers
from .views import PriceVewSet, FavoriteViewSet

router = routers.DefaultRouter()
router.register('api/v1/price_scanner/prices', PriceVewSet, 'prices')
router.register('api/v1/price_scanner/favorites', FavoriteViewSet, 'favorites')

urlpatterns = router.urls

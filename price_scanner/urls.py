from rest_framework import routers
from .views import PriceUrlVewSet


router = routers.DefaultRouter()
router.register('api/v1/price_scanner/urls', PriceUrlVewSet, 'urls')

urlpatterns = router.urls
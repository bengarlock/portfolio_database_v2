from rest_framework import routers
from .views import ImageStoreViewset

router = routers.DefaultRouter()
router.register('api/v1/image_store/', ImageStoreViewset, 'image_store')

urlpatterns = router.urls
from rest_framework import routers
from .views import JobappViewSet


router = routers.DefaultRouter()
router.register('api/v1/jobapps', JobappViewSet, 'jobapps')

urlpatterns = router.urls

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("api/v1/tablehost/books", views.BookView)
router.register("api/v1/tablehost/slots", views.SlotView)
router.register("api/v1/tablehost/restaurants", views.RestaurantView)
router.register("api/v1/tablehost/guests", views.GuestView)
router.register("api/v1/tablehost/tables", views.TableView)
router.register("api/v1/tablehost/status", views.TableView)

urlpatterns = [
    path('', include(router.urls))
]
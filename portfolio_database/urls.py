"""portfolio_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tablehost.views import BookView, SlotView, RestaurantView, GuestView, TableView
from jobapps.views import JobappViewSet
from competition_scanner.views import ResyRestaurantViewSet, ResyTotalCountViewSet, ResyCollectionViewSet, YelpRestaurantViewSet, YelpTotalCountViewSet

router = routers.DefaultRouter()

router.register("v1/tablehost/books", BookView)
router.register("v1/tablehost/slots", SlotView)
router.register("v1/tablehost/restaurants", RestaurantView)
router.register("v1/tablehost/guests", GuestView)
router.register("v1/tablehost/tables", TableView)
router.register("v1/jobapps", JobappViewSet)
router.register("v1/resy/restaurants", ResyRestaurantViewSet)
router.register("v1/resy/totals", ResyTotalCountViewSet)
router.register("v1/resy/collections", ResyCollectionViewSet)
router.register("v1/yelp/restaurants", YelpRestaurantViewSet)
router.register("v1/yelp/totals", YelpTotalCountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
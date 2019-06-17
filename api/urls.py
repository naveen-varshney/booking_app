from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'seats', SeatViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

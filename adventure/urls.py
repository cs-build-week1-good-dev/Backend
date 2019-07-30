from django.conf.urls import url
from . import api
from rest_framework import routers
from django.urls import path, include
from .models import RoomViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)


urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    path('', include(router.urls))#empty string was important here 

]
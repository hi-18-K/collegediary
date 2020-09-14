from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from .import views as projectview
from . views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', StudentViewSet)
#
# urlpatterns = [
#     path('', include('router.urls')),
#
# ]

urlpatterns = router.urls

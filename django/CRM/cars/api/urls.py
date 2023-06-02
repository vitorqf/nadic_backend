from django.urls import include, path
from rest_framework import routers

from cars.api.viewsets import CarViewSet

router = routers.DefaultRouter()
router.register(r"cars", CarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

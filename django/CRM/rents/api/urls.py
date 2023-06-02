from django.urls import include, path
from rest_framework import routers

from rents.api.viewsets import RentViewSet

router = routers.DefaultRouter()
router.register(r"rents", RentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

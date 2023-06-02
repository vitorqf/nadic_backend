from django.urls import include, path
from rest_framework import routers

from branches.api.viewsets import BranchViewSet

router = routers.DefaultRouter()
router.register(r"branches", BranchViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

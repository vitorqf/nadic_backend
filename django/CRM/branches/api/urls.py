from django.urls import include, path
from rest_framework import routers

from branches.api.viewsets import BranchViewSet

router = routers.DefaultRouter()
router.register(r"branches", BranchViewSet)

urlpatterns = [
    path("branches/rent_total/", BranchViewSet.as_view({"get": "rent_total"})),
    path(
        "branches/<int:pk>/rent_total/",
        BranchViewSet.as_view({"get": "rent_total_by_branch"}),
    ),
    path("", include(router.urls)),
]

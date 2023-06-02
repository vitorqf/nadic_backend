from django.urls import path

from CRM.api.viewsets import UserViewSet

urlpatterns = [
    path("users/create/", UserViewSet.as_view({"post": "create"})),
    path("users/login/", UserViewSet.as_view({"post": "login"})),
    path("users/logout/", UserViewSet.as_view({"post": "logout"})),
    path("users/<int:pk>/set_staff/", UserViewSet.as_view({"post": "set_staff"})),
    path("users/<int:pk>/", UserViewSet.as_view({"get": "retrieve"})),
]

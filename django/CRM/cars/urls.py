from django.urls import path

from .views import create_car, edit_car_by_id, get_car_by_id

urlpatterns = [
    path("car/<int:car_id>/", get_car_by_id, name="home"),
    path("car/create/", create_car, name="create_car"),
    path("car/<int:car_id>/edit", edit_car_by_id, name="edit_car_by_id"),
]

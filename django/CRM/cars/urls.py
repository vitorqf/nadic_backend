from django.urls import path

from .views import create_car, edit_car_by_id, get_car_by_id, list_cars

urlpatterns = [
    path("cars/", list_cars, name="list_cars"),
    path("cars/<int:car_id>/", get_car_by_id, name="get_car_by_id"),
    path("cars/create/", create_car, name="create_car"),
    path("cars/<int:car_id>/edit", edit_car_by_id, name="edit_car_by_id"),
]

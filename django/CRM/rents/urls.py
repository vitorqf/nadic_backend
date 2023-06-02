from django.urls import path

from .views import (
    create_rent,
    delete_rent_by_id,
    edit_rent_by_id,
    get_rent_by_id,
    list_rents,
)

urlpatterns = [
    path("rents/", list_rents, name="list_rents"),
    path("rents/<int:rent_id>/", get_rent_by_id, name="get_rent_by_id"),
    path("rents/<int:rent_id>/delete", delete_rent_by_id, name="delete_rent_by_id"),
    path("rents/create/", create_rent, name="create_rent"),
    path("rents/<int:rent_id>/edit", edit_rent_by_id, name="edit_rent_by_id"),
]

from django.urls import path

from .views import (create_customer, delete_customer_by_id,
                    edit_customer_by_id, get_customer_by_id, list_customers)

urlpatterns = [
    path("cars/", list_customers, name="list_customers"),
    path("cars/<int:car_id>/", get_customer_by_id, name="get_customer_by_id"),
    path("cars/<int:car_id>/delete", delete_customer_by_id, name="delete_customer_by_id"),
    path("cars/create/", create_customer, name="create_customer"),
    path("cars/<int:car_id>/edit", edit_customer_by_id, name="edit_customer_by_id"),
]

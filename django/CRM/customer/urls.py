from django.urls import path

from .views import (
    create_customer,
    delete_customer_by_id,
    edit_customer_by_id,
    get_customer_by_id,
    list_customers,
)

urlpatterns = [
    path("customers/", list_customers, name="list_customers"),
    path("customers/<int:customer_id>/", get_customer_by_id, name="get_customer_by_id"),
    path(
        "customers/<int:customer_id>/delete",
        delete_customer_by_id,
        name="delete_customer_by_id",
    ),
    path("customers/create/", create_customer, name="create_customer"),
    path(
        "customers/<int:customer_id>/edit",
        edit_customer_by_id,
        name="edit_customer_by_id",
    ),
]

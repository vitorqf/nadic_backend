from os import path


urlpatterns = [
    path("customers/", list_branches, name="list_branches"),
    path("customers/<int:customer_id>/", get_branch_by_id, name="get_branch_by_id"),
    path("customers/<int:customer_id>/delete", delete_branch_by_id, name="delete_branch_by_id"),
    path("customers/create/", create_branch, name="create_branch"),
    path("customers/<int:customer_id>/edit", edit_branch_by_id, name="edit_branch_by_id"),
]
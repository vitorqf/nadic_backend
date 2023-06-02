from django.urls import path

from .views import (
    create_branch,
    delete_branch_by_id,
    edit_branch_by_id,
    get_branch_by_id,
    list_branches,
)

urlpatterns = [
    path("branches/", list_branches, name="list_branches"),
    path("branches/<int:branch_id>/", get_branch_by_id, name="get_branch_by_id"),
    path(
        "branches/<int:branch_id>/delete",
        delete_branch_by_id,
        name="delete_branch_by_id",
    ),
    path("branches/create/", create_branch, name="create_branch"),
    path("branches/<int:branch_id>/edit", edit_branch_by_id, name="edit_branch_by_id"),
]

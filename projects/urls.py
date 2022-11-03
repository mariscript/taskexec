from django.urls import path
from projects.views import (
    project_list,
    create_project,
    delete_project,
    show_project,
    home_page,
    search_project,
)

urlpatterns = [
    path("home/", home_page, name="home_page"),
    path("", project_list, name="list_projects"),
    path("search/", search_project, name="search_project"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("delete/<int:id>/", delete_project, name="delete_project"),
]

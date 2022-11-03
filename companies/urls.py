from django.urls import path
from companies.views import (
    my_company_list,
    create_company,
    search_company,
    show_company,
    delete_company,
    join_company
)

urlpatterns = [
    path("mine/", my_company_list, name="my_company_list"),
    path("mine/<int:id>/", show_company, name="show_company"),
    path("mine/<int:id>/delete/", delete_company, name="delete_company"),
    path("create/", create_company, name="create_company"),
    path("join/", join_company, name="join_company"),
    path("search/", search_company, name="search_company"),
]

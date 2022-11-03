from django.urls import path
from companies.views import (
    my_company_list,
    create_company,
    search_company,
    show_company,
)

urlpatterns = [
    path("mine/", my_company_list, name="my_company_list"),
    path("mine/<int:id>", show_company, name="show_company"),
    path("create/", create_company, name="create_company"),
    path("search/", search_company, name="search_company"),
]

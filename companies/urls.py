from django.urls import path
from companies.views import my_company_list, create_company

urlpatterns = [
    path("mine/", my_company_list, name="my_company_list"),
    path("create/", create_company, name="create_company"),
]

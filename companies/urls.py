from django.urls import path
from companies.views import company_list, my_company_list, create_company

urlpatterns = [
    path("", company_list, name="company_list"),
    path("mine/", my_company_list, name="my_company_list"),
    path("create/", create_company, name="create_company"),
]

from django.contrib import admin
from companies.models import Company, Employee


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "company",
    )

from django.forms import ModelForm
from companies.models import Company, Employee


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ["name"]


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["company"]

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from companies.models import Company, Employee
from companies.forms import CompanyForm

# Create your views here.
# Create your views here.


@login_required
def my_company_list(request):
    companies = Company.objects.filter(owner=request.user)
    context = {
        "my_company_list": companies,
    }
    return render(request, "companies/list.html", context)


@login_required
def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid:
            company = form.save(False)
            employee = Employee.objects.create()
            company.owner, employee.name = request.user, request.user
            employee.company = company
            form.save()
            employee.save()
            return redirect("my_company_list")
    else:
        form = CompanyForm()

    context = {"form": form}
    return render(request, "companies/create.html", context)

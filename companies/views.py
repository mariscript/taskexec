from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from companies.models import Company
from django.db.models import Q
from companies.forms import CompanyForm, EmployeeForm

# Create your views here.
# Create your views here.


@login_required
def my_company_list(request):
    companies = Company.objects.all()
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
            company.owner = request.user
            form.save()
            return redirect("my_company_list")
    else:
        form = CompanyForm()

    context = {
        "form": form,
    }
    return render(request, "companies/create.html", context)


@login_required
def join_company(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(False)
            employee.owner = request.user
            form.save()
            return redirect("my_company_list")
    else:
        form = EmployeeForm()

    context = {
        "form": form,
    }
    return render(request, "companies/join.html", context)


@login_required
def delete_company(request, id):
    company = Company.objects.get(id=id)
    if request.method == "POST":
        company.delete()
        return redirect("my_company_list")

    context = {
        "single_company": company,
    }

    return render(request, "companies/delete.html", context)


@login_required
def show_company(request, id):
    show_company = Company.objects.get(id=id)
    context = {
        "show_company": show_company,
    }
    return render(request, "companies/detail.html", context)


@login_required
def search_company(request):
    query = request.GET.get("search")
    companies = Company.objects.filter(Q(name__icontains=query))
    context = {
        "results": companies,
    }
    return render(request, "companies/search.html", context)

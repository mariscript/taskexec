from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from companies.models import Company
from companies.forms import CompanyForm


# Create your views here.
def company_list(request):
    companies = Company.objects.all()
    context = {
        "company_list": companies,
    }
    return render(request, "companies/list.html", context)


@login_required
def my_company_list(request):
    companies = Company.objects.filter(employee=request.user)
    context = {
        "my_company_list": companies,
    }
    return render(request, "companies/my_list.html", context)


@login_required
def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.post)
        if form.is_valid:
            company = form.save(False)
            company.owner = request.user
            form.save()
            return redirect("my_company_list")
    else:
        form = CompanyForm()

    context = {
        "form": form
    }
    return render(request, "companies/create", context)

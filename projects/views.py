from django.shortcuts import render, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, "projects/home.html")


@login_required
def show_project(request, id):
    show_project = Project.objects.get(id=id)
    context = {
        "show_project": show_project,
    }
    return render(request, "projects/detail.html", context)


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request, request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm(request)

    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


@login_required
def delete_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        project.delete()
        return redirect("list_projects")

    context = {
        "single_project": project,
    }

    return render(request, "projects/delete.html", context)


@login_required
def search_project(request):
    query = request.GET.get("search")
    projects = Project.objects.filter(Q(name__icontains=query))
    context = {
        "results": projects,
    }
    return render(request, "projects/search.html", context)

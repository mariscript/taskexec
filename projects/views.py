from django.shortcuts import render, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


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
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)

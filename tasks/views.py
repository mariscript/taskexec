from django.shortcuts import render
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from projects.models import Project


@login_required
def show_project(request, id):
    show_project = Project.objects.filter(id=id)
    task = Task.objects.all()
    context = {
        "show_project": show_project,
        "tasks": task,
    }
    return render(request, "tasks/detail.html", context)

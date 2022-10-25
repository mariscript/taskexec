from django.shortcuts import redirect, render
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from projects.models import Project


@login_required
def show_project(request, id):
    show_project = Project.objects.get(id=id)
    tasks = Task.objects.all()
    context = {
        "show_project": show_project,
        "tasks": tasks,
    }
    return render(request, "tasks/detail.html", context)


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)

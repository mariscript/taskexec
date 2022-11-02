from django.shortcuts import redirect, render
from tasks.forms import NoteForm, TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required


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


@login_required
def task_list(request):
    task = Task.objects.filter(assignee=request.user)

    context = {
        "task_list": task,
    }
    return render(request, "tasks/list.html", context)


@login_required
def show_task(request, id):
    task = Task.objects.get(id=id)
    context = {
        "task": task,
    }
    return render(request, "tasks/detail.html", context)


@login_required
def create_note(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(False)
            note.task = task
            note.save()
            return redirect("show_task", id=id)
    else:
        form = NoteForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/edit.html", context)


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect("show_my_tasks")

    context = {
        "task": task,
    }

    return render(request, "tasks/delete.html", context)

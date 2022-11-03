from django.shortcuts import redirect, render
from tasks.forms import NoteForm, TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import pandas as pd
from plotly.offline import plot
import plotly.express as px


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm(request)

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


@login_required
def search_task(request):
    query = request.GET.get("search")
    tasks = Task.objects.filter(Q(name__icontains=query))
    context = {
        "results": tasks,
    }
    return render(request, "tasks/search.html", context)


@login_required
def task_chart(request):
    qs = Task.objects.filter(assignee=request.user)
    projects_data = [
        {
            "Task": x.name,
            "Start": x.start_date,
            "Finish": x.due_date,
            "Assignee": x.assignee,
            "Project": x.project,
        }
        for x in qs
    ]

    df = pd.DataFrame(projects_data)

    fig = px.timeline(
        df,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="Project",
        title="My Tasks",
    )

    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font_color="rgb(100, 100, 100)",
        font_family="Roboto Slab, serif",
        font_size=16,
        yaxis_title="Tasks",
        title={
            "text": "My Tasks",
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
    )

    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context = {
        "plot_div": gantt_plot,
    }
    return render(request, "tasks/chart.html", context)


def toggle(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("show_my_tasks")

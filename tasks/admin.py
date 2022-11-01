from django.contrib import admin
from tasks.models import Task, Note


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = (
        "name",
        "start_date",
        "due_date",
        "is_completed",
        "project",
        "assignee",
    )


@admin.register(Note)
class Note(admin.ModelAdmin):
    list_display = (
        "description",
        "created_on",
        "task",
    )

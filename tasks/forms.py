from django.forms import ModelForm
from tasks.models import Task, Note
from projects.models import Project


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        ]

    def __init__(self, request, *args, **kwargs):
        super(TaskForm, self).__init__(
            *args,
            **kwargs,
        )
        self.fields["project"].queryset = Project.objects.filter(
            owner=request.user
        )


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            "description",
        ]


class Checked(ModelForm):
    class Meta:
        model = Task
        fields = [
            "is_completed",
        ]

from django.forms import ModelForm
from projects.models import Project
from companies.models import Company


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "company",
        ]

    def __init__(self, request, *args, **kwargs):
        super(ProjectForm, self).__init__(
            *args,
            **kwargs,
        )
        self.fields["company"].queryset = Company.objects.filter(
            owner=request.user
        )

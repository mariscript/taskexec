from django.shortcuts import render
from projects.models import Project


def project_list(request):
    projects = Project.objects.all()
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)


# Create your views here.

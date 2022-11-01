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


def index(request):
    if Theme.objects.filter(user=request.user).exists():
        color = Theme.objects.get(user=request.user).color
    else:
        color ='blue'
    return render(request, "projects/list.html", {'color': color})


# def theme(request):
#     color = request.GET.get('color')
#     if color == 'dark':
#         if Theme.objects.filter(user=request.user).exists():
#             user_theme = Theme.objects.get(user=request.user)
#             user_theme.user = request.user
#             user_theme.color = 'grey'
#             user_theme.save()
#         else:
#             user2 = Theme(user=request.uesr, color='grey')
#             user2.save()

#     elif color == 'light':
#         if Theme.objects.filter(user=request.user).exists():
#             user_theme1 = Theme.objects.get(user=request.user)
#             user_theme1.user = request.user
#             user_theme1.color = 'white'
#             user_theme1.save()
#         else:
#             user4 = Theme(user=request.uesr, color='white')
#             user4.save()
    
#     return redirect("")

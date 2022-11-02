from django.urls import path
from tasks.views import (
    create_task,
    task_list,
    delete_task,
    show_task,
    add_task_notes,
    task_chart,
)


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", task_list, name="show_my_tasks"),
    path("mine/<int:id>/", show_task, name="show_task"),
    path("mine/edit/<int:id>/", add_task_notes, name="add_task_notes"),
    path("mine/delete/<int:id>/", delete_task, name="delete_task"),
    path("mine/chart/", task_chart, name="task_chart"),
]

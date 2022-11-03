from django.urls import path
from tasks.views import (
    create_task,
    task_list,
    delete_task,
    show_task,
    create_note,
    task_chart,
    search_task,
    toggle,
)


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", task_list, name="show_my_tasks"),
    path("mine/search/", search_task, name="search_task"),
    path("mine/<int:id>/", show_task, name="show_task"),
    path("mine/<int:id>/toggle/", toggle, name="toggle_task"),
    path("mine/edit/<int:id>/", create_note, name="create_note"),
    path("mine/delete/<int:id>/", delete_task, name="delete_task"),
    path("mine/chart/", task_chart, name="task_chart"),
]

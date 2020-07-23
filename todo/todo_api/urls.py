from django.urls import path
from . import views

app_name = 'todo_api'

urlpatterns = [
    path("", views.IndexAPIView.as_view(), name="index"),
    path("task/<int:pk>", views.TaskAPIDetailView.as_view(), name='task_detail'),
    path("tasks/", views.TaskAPIListView.as_view(), name='tasks_list')
]
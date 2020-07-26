from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("project", views.ProjectViewSet)

app_name = 'todo_api'

urlpatterns = [
    path("", views.IndexAPIView.as_view(), name="index"),
    path("task/<int:pk>", views.TaskAPIDetailView.as_view(), name='task_detail'),
    path("tasks/", views.TaskAPIListView.as_view(), name='tasks_list'),
    path("project/<int:pk>", views.ProjectAPIView.as_view(), name='project'),
    path("viewset/", include(router.urls))
]
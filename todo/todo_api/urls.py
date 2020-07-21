from django.urls import path
from . import views

app_name = 'todo_api'

urlspatterns = [
    path("", views, namne="index")
]
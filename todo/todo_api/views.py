from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import ToDoTaskSerializer, ProjectSerrializer
from todo_app.models import ToDoTask, Project
# Create your views here.

class IndexAPIView(views.APIView):

    def get(self, request):
        task = get_object_or_404(ToDoTask, pk=1)
        data_object = ToDoTaskSerializer(task)
        return Response(data_object.data)

class TaskAPIDetailView(views.APIView):
    def get(self, request, pk):
        task = get_object_or_404(ToDoTask, pk=pk)
        serialized_task = ToDoTaskSerializer(task)
        return Response(serialized_task.data)


class TaskAPIListView(views.APIView):
    def get(self, request):
        tasks_list = ToDoTask.objects.all()
        serialized_tasks_list = ToDoTaskSerializer(tasks_list, many=True)
        return Response(serialized_tasks_list.data)

    def post(self, request):
        data = ToDoTaskSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerrializer
    queryset = Project.objects.all()
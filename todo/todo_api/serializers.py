from rest_framework import serializers
from todo_app.models import ToDoTask

class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = 'id', 'is_complited', 'title', 'description'
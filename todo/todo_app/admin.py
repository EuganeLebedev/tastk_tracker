from django.contrib import admin

# Register your models here.

from .models import ToDoTask, Project


@admin.register(ToDoTask)
class ToDoTaskAdmin(admin.ModelAdmin):
    list_display = ['is_complited', 'title']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ['title']

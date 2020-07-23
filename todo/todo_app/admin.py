from django.contrib import admin

# Register your models here.

from .models import ToDoTask

@admin.register(ToDoTask)
class ToDoTaskAdmin(admin.ModelAdmin):
    list_display = ['is_complited', 'title']
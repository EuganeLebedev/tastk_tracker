from django.db import models

# Create your models here.

class ToDoTask(models.Model):
    is_complited = models.BooleanField(default=False)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

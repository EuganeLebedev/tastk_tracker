from django.db import models

# Create your models here.

class ToDoTask(models.Model):
    is_complited = models.BooleanField(default=False)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return f"{self.id} {self.title}"


from django.db import models
import datetime


class TodoList(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, null=True, default="My Tasks")
    deadline = models.DateField(default=datetime.date.today)
    done = models.BooleanField(default=False)

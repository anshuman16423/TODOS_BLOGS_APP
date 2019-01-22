from django.db import models


class Task(models.Model):
    username = models.CharField(max_length=50)
    task_title = models.CharField( max_length=50)
    task_detail = models.TextField(max_length=150)


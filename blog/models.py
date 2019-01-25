from django.db import models


# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=64)
    tags = models.CharField(max_length=256)
    content = models.TextField(max_length=512)

from django.db import models
import datetime


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField(default=datetime.date.today())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
# Create your models here.

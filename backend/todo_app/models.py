from django.db import models
from django.utils import timezone

class List(models.Model):
    title = models.CharField(max_length=64)
    user = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.title}"

class Task(models.Model):
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return f"{self.description}: Due: {self.due_date}"



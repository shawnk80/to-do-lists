## wines/serializers.py
from rest_framework import serializers
from .models import List, Task

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['title', 'user', 'tasks']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'completed', 'due_date', 'list']

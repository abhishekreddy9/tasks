from rest_framework import serializers
from .models import TaskGroup, Task


class TaskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGroup
        fields = ('title', 'user')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('content', 'tasks')

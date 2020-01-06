from django.shortcuts import render
from rest_framework import viewsets
from .models import TaskGroup, Task
from .serializers import TaskGroupSerializer, TaskSerializer


class TaskGroupViewSet(viewsets.ModelViewSet):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

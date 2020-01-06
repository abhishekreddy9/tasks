from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import TaskGroup, Task, User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import TaskGroupSerializer, TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskGroupViewSet(viewsets.ModelViewSet):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

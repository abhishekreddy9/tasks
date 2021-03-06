from django.shortcuts import render
from .models import User, TaskGroup, Task
from rest_framework import viewsets, generics, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import TaskGroupSerializer, TaskSerializer, UserSerializer
from api import permissions


"""----------------------------USER VIEWS--------------------------------"""
class UserViewSet(mixins.CreateModelMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




"""----------------------------TASKGROUP VIEWS--------------------------------"""



"""TASKGROUP-GET-UPDATE-DELETE"""
class TaskGroupViewSetGetDeleteUpdate(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, permissions.UpdateOwnProfile]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""TASKGROUP CREATE"""
class TaskGroupViewSetPost(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, permissions.UpdateOwnProfile]

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



"""----------------------------TASK VIEWS--------------------------------"""


"""TASK-GET ALL TASKS BY TASKGROUP"""
class TaskViewSet(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    # queryset = query.filter
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def get_queryset(self):
        key = self.request.query_params['id']
        if(TaskGroup.objects.all().filter(id=key).filter(user=self.request.user)):
            return self.queryset.filter(taskgroupid=key)
        else:
            return None

"""CREATE TASK"""
class AddTask(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    # queryset = query.filter
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        taskgroupid = request.data['taskgroupid']
        query = TaskGroup.objects.filter(id=taskgroupid)
        if(query.filter(user=request.user)):
            return self.create(request, *args, **kwargs)
        else:
            return Response(data={'message': 'not Allowed'}, status=None, template_name=None, headers=None, content_type=None)


"""GET,EDIT,DELETE A PARTICULAR TASK"""
class TaskViewGetEditDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
     
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
       

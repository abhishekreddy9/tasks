from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TaskGroupViewSetGetDeleteUpdate, TaskViewSet, UserViewSet, TaskGroupViewSetPost, AddTask, TaskGroupViewSetGetDeleteUpdate,TaskViewGetEditDelete


urlpatterns = [
    path('taskgroup/<pk>', TaskGroupViewSetGetDeleteUpdate.as_view(),
         name='task-group-get'),
    path('taskgroup', TaskGroupViewSetPost.as_view(), name='task-group-post'),
    path('tasks', TaskViewSet.as_view(), name='task'),
    path('createtask', AddTask.as_view(), name='tasks'),
    path('task/<pk>', TaskViewGetEditDelete.as_view(), name='eachtask'),
    path('user', UserViewSet.as_view(), name='usercreate')
]


# , TaskGroupViewSetDelete

# router = routers.DefaultRouter()
#router.register('taskgrp', TaskGroupViewSetPost)
# router.register('task', TaskViewSet)
# router.register('user', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# path('', include(router.urls))

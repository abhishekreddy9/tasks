from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TaskGroupViewSetGetDeleteUpdate, TaskViewSet, UserViewSet, TaskGroupViewSetPost
# , TaskGroupViewSetDelete

#router = routers.DefaultRouter()
#router.register('taskgrp', TaskGroupViewSetPost)
# router.register('task', TaskViewSet)
# router.register('user', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('taskgroup/<pk>', TaskGroupViewSetGetDeleteUpdate.as_view(),
         name='task-group-get'),
    path('taskgroup', TaskGroupViewSetPost.as_view(), name='task-group-post'),
    path('task', TaskViewSet.as_view(), name='tasks')

]

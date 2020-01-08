from rest_framework import permissions
from .models import TaskGroup, User, Task


class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print(obj.user.id)
        if obj.user.id == request.user.id:
            return True

        else:
            return False

        # # Instance must have an attribute named `owner`.
        # return obj.owner == request.user


# class VerifyChild(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         temp = obj.tasks
#         if TaskGroup.objects.all.filter(id=temp).filter(user=request.user):
#             print('hiiiiii')
#             return True

#         else:
#             return False

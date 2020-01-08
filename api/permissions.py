from rest_framework import permissions


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

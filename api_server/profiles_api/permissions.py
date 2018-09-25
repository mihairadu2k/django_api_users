from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """check if user is changing the user profile"""
        print(request)
        print(view)
        print(obj)

        if request.method in permissions.SAFE_METHODS:
            return True


        return obj.id == request.user.id

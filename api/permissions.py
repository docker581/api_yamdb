from rest_framework import permissions


class IsSuperuserPermissionOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_anonymous:
            return (
                obj.author == request.user
                or request.user.is_superuser
                or request.user.role == 'admin'
                or request.user.role == 'moderator'
            )
        else:
            return (
                request.method in permissions.SAFE_METHODS
            )

from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    ADMIN = 'admin'

    def has_permission(self, request, view):
        return request.user.role == self.ADMIN or request.user.is_superuser

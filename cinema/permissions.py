from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class IsAdminOrIfAuthenticatedReadOnly(IsAuthenticated):
    """
    The request is authenticated as a user, or is a read-only.
    """
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff

class IsAuthenticatedOrAdmin(BasePermission):
    """
    Full access for authenticated users.
    Full access for admins.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

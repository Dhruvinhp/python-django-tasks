from rest_framework.permissions import BasePermission


class PostPermission(BasePermission):
    """
    Custom permission class for Quiz add
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user.is_authenticated

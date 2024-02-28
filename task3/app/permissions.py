from rest_framework.permissions import BasePermission


class QuizPermission(BasePermission):
    """
    Custom permission class for Quiz add
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user.is_authenticated

from rest_framework.permissions import BasePermission


class QuizPermission(BasePermission):
    """
    Custom permission class for Quiz add
    """

    def has_permission(self, request, view):
        return request.method == "POST"

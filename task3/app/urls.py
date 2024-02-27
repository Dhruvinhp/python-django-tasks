from django.urls import path, include
from .views import (
    UserView,
    QuizListView,
    UserQuizListView,
    QuizDetailView,
    CompleteQuizView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register("user", UserView, basename="users")

urlpatterns = [
    path("", include(routers.urls), name="apis"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("quizzes/", QuizListView.as_view(), name="quiz-list"),
    path("user/quizzes/", UserQuizListView.as_view(), name="user-quiz-list"),
    path("quizzes/<int:pk>/", QuizDetailView.as_view(), name="quiz-detail"),
    path(
        "quizzes/<int:pk>/complete/", CompleteQuizView.as_view(), name="complete-quiz"
    ),
]

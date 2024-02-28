from django.urls import path, include
from .views import (
    UserView,
    QuizListView,
    UserQuizListView,
    CompleteQuizView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register("user", UserView, basename="users")
routers.register("quizzes", QuizListView, basename="quiz-list")

urlpatterns = [
    path("", include(routers.urls), name="apis"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user-quizzes/", UserQuizListView.as_view(), name="user-quiz-list"),
    path(
        "complete-quiz/<int:pk>/",
        CompleteQuizView.as_view(),
        name="complete-quiz",
    ),
]

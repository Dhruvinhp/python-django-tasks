from django.urls import path
from .views import (
    RegisterView,
    QuizListView,
    UserQuizListView,
    QuizDetailView,
    CompleteQuizView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("quizzes/", QuizListView.as_view(), name="quiz-list"),
    path("user/quizzes/", UserQuizListView.as_view(), name="user-quiz-list"),
    path("quizzes/<int:pk>/", QuizDetailView.as_view(), name="quiz-detail"),
    path(
        "quizzes/<int:pk>/complete/", CompleteQuizView.as_view(), name="complete-quiz"
    ),
]

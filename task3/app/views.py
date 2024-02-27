from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Quiz, UserQuiz, User
from .serializers import (
    UserSerializer,
    QuizSerializer,
    UserQuizSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        quizzes = Quiz.objects.all()[:5]
        for quiz in quizzes:
            UserQuiz.objects.create(user=user, quiz=quiz)


class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserQuizListView(generics.ListAPIView):
    serializer_class = UserQuizSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return UserQuiz.objects.filter(user=user)


class QuizDetailView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        quiz_id = kwargs.get("pk")
        try:
            current_quiz = Quiz.objects.get(pk=quiz_id)
            previous_quiz_id = current_quiz.id - 1
            if previous_quiz_id > 0:
                try:
                    previous_user_quiz = UserQuiz.objects.get(
                        user=user, quiz_id=previous_quiz_id
                    )
                    if not previous_user_quiz.completed:
                        return Response(
                            {"error": "Complete the previous quiz first."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                except UserQuiz.DoesNotExist:
                    return Response(
                        {"error": "Complete the previous quiz first."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().get(request, *args, **kwargs)


class CompleteQuizView(generics.UpdateAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        quiz_id = instance.quiz_id
        try:
            current_quiz = Quiz.objects.get(pk=quiz_id)
            previous_quiz_id = current_quiz.id - 1
            if previous_quiz_id > 0:
                try:
                    previous_user_quiz = UserQuiz.objects.get(
                        user=user, quiz_id=previous_quiz_id
                    )
                    if not previous_user_quiz.completed:
                        return Response(
                            {"error": "Complete the previous quiz first."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                except UserQuiz.DoesNotExist:
                    return Response(
                        {"error": "Complete the previous quiz first."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            instance.completed = True
            instance.save()
            return Response("Quiz completed successfully")
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
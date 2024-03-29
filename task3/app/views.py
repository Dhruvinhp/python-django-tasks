from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .permissions import PostPermission

from .models import Quiz, UserQuiz, User
from .serializers import (
    UserSerializer,
    QuizSerializer,
    UserQuizSerializer,
)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [PostPermission]

    def perform_create(self, serializer):
        data = self.request.data.copy()
        user = serializer.save(password=make_password(data["password"]))
        quizzes = Quiz.objects.all()[:5]
        for quiz in quizzes:
            UserQuiz.objects.create(user=user, quiz=quiz)


class QuizListView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [PostPermission]

    def retrieve(self, request, *args, **kwargs):
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

        serializer = self.get_serializer(current_quiz)
        return Response(serializer.data)


class UserQuizListView(generics.ListAPIView):
    serializer_class = UserQuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserQuiz.objects.filter(user=user)


class CompleteQuizView(generics.UpdateAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer
    permission_classes = [IsAuthenticated]

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

            if instance.completed:
                return Response(
                    {"error": "Quiz is already completed."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            instance.completed = True
            instance.save()

            return Response(
                {"message": "Quiz completed successfully"}, status=status.HTTP_200_OK
            )
        except Quiz.DoesNotExist:
            return Response(
                {"error": "Quiz does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

from rest_framework import serializers
from .models import Quiz, UserQuiz, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("id", "name")


class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = ("id", "user", "quiz", "completed")

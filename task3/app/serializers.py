from rest_framework import serializers

from .validators import PasswordValidator
from .models import Quiz, UserQuiz, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[PasswordValidator()])

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("password", None)
        return ret


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("id", "name")


class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = ("id", "user", "quiz", "completed")

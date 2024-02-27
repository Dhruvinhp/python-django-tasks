from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quiz(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name


class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "User Quizzes"

    def __str__(self):
        return self.user.username + " - " + self.quiz.name

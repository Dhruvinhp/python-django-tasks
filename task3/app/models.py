from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quiz(models.Model):
    name = models.CharField(max_length=100)


class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

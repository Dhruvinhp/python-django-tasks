from django.contrib import admin
from .models import Quiz, User, UserQuiz


admin.site.register(Quiz)
admin.site.register(User)
admin.site.register(UserQuiz)

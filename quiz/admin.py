from django.contrib import admin
from .models import Question, QuizSession, UserResponse

# Register your models here.

admin.site.register(Question)
admin.site.register(QuizSession)
admin.site.register(UserResponse)

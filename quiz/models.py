from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_answer = models.IntegerField()  # 1, 2, 3, or 4
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class UserResponse(models.Model):
    session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.IntegerField()
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-answered_at']

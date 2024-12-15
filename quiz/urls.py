from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/', views.get_random_question, name='get_question'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('stats/', views.get_stats, name='get_stats'),
]

from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, QuizSession, UserResponse
import random
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def start_quiz(request):
    # Create a new quiz session
    session = QuizSession.objects.create()
    return JsonResponse({'session_id': session.id})

def get_random_question(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return JsonResponse({'error': 'Session ID is required'}, status=400)
    
    # Get session
    try:
        session = QuizSession.objects.get(id=session_id, is_active=True)
    except QuizSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid or expired session'}, status=400)

    # Get answered questions in this session
    answered_questions = UserResponse.objects.filter(session=session).values_list('question_id', flat=True)
    
    # Get a random unanswered question
    available_questions = Question.objects.exclude(id__in=answered_questions)
    if not available_questions.exists():
        return JsonResponse({'message': 'No more questions available'}, status=404)
    
    question = random.choice(available_questions)
    return JsonResponse({
        'id': question.id,
        'question': question.question_text,
        'options': [
            question.option_1,
            question.option_2,
            question.option_3,
            question.option_4
        ]
    })

@csrf_exempt
def submit_answer(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    
    data = json.loads(request.body)
    session_id = data.get('session_id')
    question_id = data.get('question_id')
    selected_answer = data.get('answer')

    try:
        session = QuizSession.objects.get(id=session_id, is_active=True)
        question = Question.objects.get(id=question_id)
    except (QuizSession.DoesNotExist, Question.DoesNotExist):
        return JsonResponse({'error': 'Invalid session or question'}, status=400)

    # Check if already answered
    if UserResponse.objects.filter(session=session, question=question).exists():
        return JsonResponse({'error': 'Question already answered'}, status=400)

    # Create response
    is_correct = (selected_answer == question.correct_answer)
    UserResponse.objects.create(
        session=session,
        question=question,
        selected_answer=selected_answer,
        is_correct=is_correct
    )

    return JsonResponse({
        'correct': is_correct,
        'correct_answer': question.correct_answer
    })

def get_stats(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return JsonResponse({'error': 'Session ID is required'}, status=400)

    try:
        session = QuizSession.objects.get(id=session_id)
    except QuizSession.DoesNotExist:
        return JsonResponse({'error': 'Invalid session'}, status=400)

    responses = UserResponse.objects.filter(session=session)
    total_questions = responses.count()
    correct_answers = responses.filter(is_correct=True).count()

    return JsonResponse({
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': total_questions - correct_answers,
        'score_percentage': (correct_answers / total_questions * 100) if total_questions > 0 else 0
    })

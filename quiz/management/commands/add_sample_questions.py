from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Adds sample questions to the database'

    def handle(self, *args, **kwargs):
        questions = [
            {
                'question_text': 'What is the capital of France?',
                'option_1': 'London',
                'option_2': 'Paris',
                'option_3': 'Berlin',
                'option_4': 'Madrid',
                'correct_answer': 2
            },
            {
                'question_text': 'Which planet is known as the Red Planet?',
                'option_1': 'Venus',
                'option_2': 'Jupiter',
                'option_3': 'Mars',
                'option_4': 'Saturn',
                'correct_answer': 3
            },
            {
                'question_text': 'What is 2 + 2?',
                'option_1': '3',
                'option_2': '4',
                'option_3': '5',
                'option_4': '6',
                'correct_answer': 2
            },
            {
                'question_text': 'Who painted the Mona Lisa?',
                'option_1': 'Leonardo da Vinci',
                'option_2': 'Pablo Picasso',
                'option_3': 'Vincent van Gogh',
                'option_4': 'Michelangelo',
                'correct_answer': 1
            },
            {
                'question_text': 'What is the largest mammal in the world?',
                'option_1': 'African Elephant',
                'option_2': 'Blue Whale',
                'option_3': 'Giraffe',
                'option_4': 'Polar Bear',
                'correct_answer': 2
            }
        ]

        for question_data in questions:
            Question.objects.create(**question_data)
            self.stdout.write(self.style.SUCCESS(f'Added question: {question_data["question_text"]}'))

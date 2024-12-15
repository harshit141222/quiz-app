let currentSession = null;
let currentQuestion = null;

document.addEventListener('DOMContentLoaded', () => {
    // Add event listeners
    document.getElementById('start-quiz').addEventListener('click', startQuiz);
    document.getElementById('submit-answer').addEventListener('click', submitAnswer);
    document.getElementById('next-question').addEventListener('click', getNextQuestion);
    
    // Initially hide the quiz content and stats
    document.querySelector('.quiz-content').classList.add('hidden');
    document.querySelector('.stats').classList.add('hidden');
});

async function startQuiz() {
    try {
        const response = await fetch('/api/start/');
        const data = await response.json();
        currentSession = data.session_id;
        
        // Show quiz content and hide start button
        document.querySelector('.quiz-content').classList.remove('hidden');
        document.getElementById('start-quiz').classList.add('hidden');
        
        // Get first question
        await getNextQuestion();
    } catch (error) {
        showMessage('Error starting quiz. Please try again.', 'error');
    }
}

async function getNextQuestion() {
    try {
        const response = await fetch(`/api/question/?session_id=${currentSession}`);
        const data = await response.json();
        
        if (response.status === 404) {
            endQuiz();
            return;
        }
        
        currentQuestion = data;
        displayQuestion(data);
        
        // Reset UI state
        document.getElementById('submit-answer').classList.remove('hidden');
        document.getElementById('next-question').classList.add('hidden');
        clearOptionStyles();
    } catch (error) {
        showMessage('Error getting question. Please try again.', 'error');
    }
}

function displayQuestion(question) {
    document.querySelector('.question').textContent = question.question;
    const optionsContainer = document.querySelector('.options');
    optionsContainer.innerHTML = '';
    
    question.options.forEach((option, index) => {
        const optionElement = document.createElement('div');
        optionElement.className = 'option';
        optionElement.textContent = option;
        optionElement.dataset.value = index + 1;
        optionElement.addEventListener('click', selectOption);
        optionsContainer.appendChild(optionElement);
    });
}

function selectOption(event) {
    clearOptionStyles();
    event.target.classList.add('selected');
}

function clearOptionStyles() {
    document.querySelectorAll('.option').forEach(option => {
        option.classList.remove('selected', 'correct', 'incorrect');
    });
}

async function submitAnswer() {
    const selectedOption = document.querySelector('.option.selected');
    if (!selectedOption) {
        showMessage('Please select an answer', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/submit/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                session_id: currentSession,
                question_id: currentQuestion.id,
                answer: parseInt(selectedOption.dataset.value)
            })
        });
        
        const data = await response.json();
        
        // Show correct/incorrect answers
        document.querySelectorAll('.option').forEach(option => {
            const optionValue = parseInt(option.dataset.value);
            if (optionValue === data.correct_answer) {
                option.classList.add('correct');
            } else if (option.classList.contains('selected') && !data.correct) {
                option.classList.add('incorrect');
            }
        });
        
        // Update UI
        document.getElementById('submit-answer').classList.add('hidden');
        document.getElementById('next-question').classList.remove('hidden');
        
        // Update stats
        await updateStats();
    } catch (error) {
        showMessage('Error submitting answer. Please try again.', 'error');
    }
}

async function updateStats() {
    try {
        const response = await fetch(`/api/stats/?session_id=${currentSession}`);
        const data = await response.json();
        
        document.querySelector('.stats').classList.remove('hidden');
        document.getElementById('total-questions').textContent = data.total_questions;
        document.getElementById('correct-answers').textContent = data.correct_answers;
        document.getElementById('incorrect-answers').textContent = data.incorrect_answers;
        document.getElementById('score-percentage').textContent = `${Math.round(data.score_percentage)}%`;
    } catch (error) {
        console.error('Error updating stats:', error);
    }
}

function endQuiz() {
    document.querySelector('.quiz-content').classList.add('hidden');
    showMessage('Quiz completed! Check your final stats below.', 'success');
    updateStats();
}

function showMessage(message, type) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${type}`;
    messageElement.textContent = message;
    
    const container = document.querySelector('.container');
    container.insertBefore(messageElement, container.firstChild);
    
    setTimeout(() => {
        messageElement.remove();
    }, 3000);
}

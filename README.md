# Interactive Quiz Application

A beautiful and interactive quiz application built with Django and modern web technologies.

## Features

- Modern, responsive user interface
- Real-time feedback on answers
- Statistics dashboard
- Multiple choice questions
- Admin interface for managing questions
- Beautiful animations and transitions

## Technologies Used

- Django 5.0
- Python 3.11+
- HTML5
- CSS3
- JavaScript (ES6+)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/quiz-app.git
cd quiz-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

5. Add sample questions:
```bash
python manage.py add_sample_questions
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.
Visit `http://localhost:8000/admin` to access the admin interface.

## Project Structure

- `quiz/` - Main application directory
  - `models.py` - Database models for questions and responses
  - `views.py` - View functions for handling requests
  - `urls.py` - URL routing
- `static/` - Static files (CSS, JavaScript)
- `templates/` - HTML templates
- `requirements.txt` - Project dependencies

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Quiz App - Local Setup Guide
============================

Prerequisites:
-------------
1. Python 3.9 or higher installed on your system
2. pip (Python package manager)
3. Git (optional, for cloning the repository)

Step 1: Get the Project
----------------------
Option A - Clone from GitHub:
1. Open terminal/command prompt
2. Run: git clone https://github.com/YOUR_USERNAME/quiz-app.git
3. cd quiz-app

Option B - Download ZIP:
1. Download the project ZIP from GitHub
2. Extract to your desired location
3. Open terminal/command prompt in the extracted folder

Step 2: Set Up Python Environment
-------------------------------
1. Install required packages:
   python -m pip install -r requirements.txt

Step 3: Configure Environment Variables
------------------------------------
1. Create a file named '.env' in the project root
2. Add the following content:
   DEBUG=True
   SECRET_KEY=django-insecure-4acx-q1-xwu-#s&tcd9&q5)5=2lxn%@i38d0e(ddl4_=&nshww
   ALLOWED_HOSTS=localhost,127.0.0.1

Step 4: Database Setup
--------------------
1. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

2. Create admin user:
   python manage.py createsuperuser
   - Enter username (e.g., admin)
   - Enter email (e.g., admin@example.com)
   - Enter password (e.g., admin)

Step 5: Run the Development Server
--------------------------------
1. Start the server:
   python manage.py runserver

2. Access the application:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin

Step 6: Adding Quiz Content
-------------------------
1. Go to http://127.0.0.1:8000/admin
2. Log in with your superuser credentials
3. Click on "Questions" to add new questions
4. Add questions with:
   - Question text
   - Options (A, B, C, D)
   - Correct answer

Using the Quiz App
-----------------
1. Students can:
   - View available quizzes
   - Take quizzes
   - See their scores
   - Review their answers

2. Administrators can:
   - Add/Edit questions
   - View student results
   - Manage user accounts

Troubleshooting
--------------
1. If packages fail to install:
   - Try: pip install --upgrade pip
   - Then retry: pip install -r requirements.txt

2. If database errors occur:
   - Delete db.sqlite3 file
   - Delete all files in migrations folders except __init__.py
   - Run migrations again (Step 4)

3. If server won't start:
   - Check if port 8000 is in use
   - Try: python manage.py runserver 8001

Need Help?
---------
For issues or questions:
1. Check the Django documentation: https://docs.djangoproject.com/
2. Visit the project repository
3. Contact the project maintainer

Stopping the Application
----------------------
1. To stop the server: Press Ctrl+C in the terminal
2. Close the terminal window

Note: This is a development setup. For production deployment, additional security measures should be implemented.

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')

# Run migrations and collect static files
if os.environ.get('VERCEL_ENV') == 'production':
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    execute_from_command_line(['manage.py', 'migrate'])

# Initialize Django WSGI application
application = get_wsgi_application()

# Export the WSGI application
app = application

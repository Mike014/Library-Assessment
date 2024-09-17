import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryassessment.settings')
django.setup()

username = 'admin'
email = 'admin@example.com'
password = 'adminpassword'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created successfully.')
else:
    print('Superuser already exists.')

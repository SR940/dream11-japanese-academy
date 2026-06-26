import os
from django.core.wsgi import get_wsgi_application

# Ensure this points to your exact settings file location
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

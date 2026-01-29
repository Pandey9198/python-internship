"""
ASGI config for todo_project project.
<<<<<<< HEAD

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
=======
>>>>>>> 57d8d5c (Add todo_project folder)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

application = get_asgi_application()

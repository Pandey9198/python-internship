<<<<<<< HEAD
=======
"""
URL configuration for todo_project project.
"""
>>>>>>> 57d8d5c (Add todo_project folder)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('todo.urls')),
=======
    path('', include('todo_app.urls')),
>>>>>>> 57d8d5c (Add todo_project folder)
]

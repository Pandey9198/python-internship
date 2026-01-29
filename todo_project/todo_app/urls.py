"""
URL configuration for todo_app application.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('create/', views.create_todo, name='create_todo'),
    path('todo/<int:pk>/update/', views.update_todo, name='update_todo'),
    path('todo/<int:pk>/delete/', views.delete_todo, name='delete_todo'),
    path('todo/<int:pk>/toggle/', views.toggle_todo_status, name='toggle_todo'),
]

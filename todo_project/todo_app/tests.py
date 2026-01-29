"""
Tests for the todo_app application.
"""
from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    """Test cases for the Todo model."""
    
    def setUp(self):
        """Create a sample Todo for testing."""
        Todo.objects.create(
            title='Test Todo',
            description='This is a test todo',
            status='pending'
        )
    
    def test_todo_creation(self):
        """Test that a Todo can be created."""
        todo = Todo.objects.get(title='Test Todo')
        self.assertEqual(todo.status, 'pending')
    
    def test_todo_str_representation(self):
        """Test the string representation of Todo."""
        todo = Todo.objects.get(title='Test Todo')
        self.assertEqual(str(todo), 'Test Todo')

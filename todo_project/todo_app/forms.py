"""
Forms for the todo_app application.
"""
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    """Form for creating and updating Todo items."""
    
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter todo title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description (optional)'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

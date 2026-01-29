"""
Views for the todo_app application.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    """Display list of all todos."""
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todo_list.html', context)


def todo_detail(request, pk):
    """Display detail of a specific todo."""
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todo_detail.html', context)


def create_todo(request):
    """Create a new todo item."""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'create_todo.html', context)


def update_todo(request, pk):
    """Update an existing todo item."""
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'update_todo.html', context)


def delete_todo(request, pk):
    """Delete a todo item."""
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    context = {
        'todo': todo,
    }
    return render(request, 'delete_todo.html', context)


@require_http_methods(["POST"])
def toggle_todo_status(request, pk):
    """Toggle the status of a todo item."""
    todo = get_object_or_404(Todo, pk=pk)
    todo.status = 'completed' if todo.status == 'pending' else 'pending'
    todo.save()
    return redirect('todo_list')

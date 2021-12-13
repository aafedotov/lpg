from django.shortcuts import render, redirect, reverse
from .forms import TaskForm
from .models import Task

from django.shortcuts import get_object_or_404


def todo_list(request):
    """View-функция главной страницы с задачами."""
    template = 'todo/todo_list.html'
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.save()
        return redirect('todo:list')
    tasks = Task.objects.all()
    return render(request, template, {'form': form, 'tasks': tasks})


def task_close(request, task_id):
    """View-функция для закрытия задач."""
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('todo:list')

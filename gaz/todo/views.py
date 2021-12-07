from django.shortcuts import render, redirect, reverse


def todo_list(request):
    """View-функция успешное добавление данных о заправке."""
    template = 'todo/todo_list.html'
    return render(request, template)

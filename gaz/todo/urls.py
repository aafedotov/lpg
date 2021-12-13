from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todo_list, name='list'),
    path('task_close/<int:task_id>/', views.task_close, name='task_close'),
]

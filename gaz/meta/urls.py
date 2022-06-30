from django.urls import path
from . import views

app_name = 'meta'

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.meta_success, name='success')
]

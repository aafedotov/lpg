from django.urls import path
from . import views

app_name = 'lpg'
urlpatterns = [
    path('', views.lpg_view, name='lpg_view'),
    path('summary/', views.lpg_summary, name='lpg_summary'),
    path('success/', views.lpg_success, name='success')
]
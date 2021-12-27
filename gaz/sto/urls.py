from django.urls import path
from . import views

app_name = 'sto'
urlpatterns = [
    path('', views.sto_view, name='sto_view'),
    path('summary/', views.sto_summary, name='sto_summary'),
    path('success/', views.sto_success, name='success')
]
from django.urls import path
from . import views


app_name = 'petrol'
urlpatterns = [
    path('', views.petrol_view, name='petrol_view'),
    path('summary/', views.petrol_summary, name='petrol_summary'),
    path('success/', views.petrol_success, name='success')
]

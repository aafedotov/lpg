from django.urls import path
from lpg import views

app_name = 'lpg'
urlpatterns = [
    path('', views.lpg_view, name='lpg_view'),
]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lpg/', include('lpg.urls', namespace='lpg')),
    path('sto/', include('sto.urls', namespace='sto')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

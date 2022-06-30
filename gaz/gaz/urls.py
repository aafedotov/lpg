from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views, settings

urlpatterns = [
    path('', views.index, name='index'),
    path('lpg/', include('lpg.urls', namespace='lpg')),
    path('sto/', include('sto.urls', namespace='sto')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('meta/', include('meta.urls', namespace='meta')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('status/', views.status_check, name='status_check'),
    path('admin/', admin.site.urls),
]

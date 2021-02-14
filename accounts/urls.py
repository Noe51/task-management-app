from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('check/', views.check, name='check'),
    path('task/<str:pk>/', views.updateTask, name='task-details'),


    path('clients', views.clients, name='clients'),
    
]
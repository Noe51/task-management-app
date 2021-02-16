from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('check/', views.check, name='check'),

    path('task/update/<str:pk>/', views.updateTask, name='task-details'),
    path('task/delete/<str:pk>/', views.deleteTask, name='delete'),



    path('clients', views.clients, name='clients'),
    
]
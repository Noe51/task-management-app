from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('check/', views.check, name='check'),

    path('task/update/<str:pk>/', views.updateTask, name='task-details'),
    path('task/delete/<str:pk>/', views.deleteTask, name='task-delete'),

    path('client/update/<str:pk>/', views.updateClient, name='client-details'),
    path('client/delete/<str:pk>/', views.deleteClient, name='client-delete'),

    path('fund/update/<str:pk>/', views.updateFund, name='fund-details'),
    path('fund/delete/<str:pk>/', views.deleteFund, name='fund-delete'),

    path('clients/', views.clients, name='clients'),
    path('funds/', views.funds, name='funds'),
    
]
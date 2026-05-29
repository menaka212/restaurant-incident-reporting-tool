from django.urls import path
from . import views

urlpatterns = [
    path('check-users/', views.check_users, name='check_users'),
    
]
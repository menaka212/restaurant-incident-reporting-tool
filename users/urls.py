from django.urls import path
from . import views

urlpatterns = [
    path('check-users/', views.check_users, name='check_users'),
    path('create-admin/', views.create_admin, name='create_admin'), 
    path('create-users/', views.create_users, name='create_users'),
]
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.models import User
from django.http import HttpResponse

def check_users(request):
    users = User.objects.all()

    output = f"Total Users: {users.count()}<br><br>"

    for user in users:
        output += f"{user.username}<br>"

    return HttpResponse(output)
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    try:
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@gmail.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )

        if created:
            admin_user.set_password('Admin@123')
            admin_user.save()

        return HttpResponse(
            f"Total users in database: {User.objects.count()}"
        )

    except Exception as e:
        return HttpResponse(f"ERROR: {e}")
    
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_users(request):

    if not User.objects.filter(username='staff1').exists():
        User.objects.create_user(
            username='staff1',
            password='Staff@123'
        )

    if not User.objects.filter(username='manager').exists():
        User.objects.create_user(
            username='manager',
            password='Manager@123'
        )

    return HttpResponse("Users Created")

from django.contrib.auth.models import User
from django.http import HttpResponse

def check_passwords(request):
    user = User.objects.first()

    return HttpResponse(user.password)
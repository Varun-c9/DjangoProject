from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User
from .forms import UserForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_detail')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')


def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Error creating user.')
    return render(request, 'signup.html', {'form': form})


def user_detail_view(request):
    users = User.objects.all()
    return render(request, 'user_detail.html', {'users': users})


def edit_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_detail')
        else:
            messages.error(request, 'Error updating user.')
    return render(request, 'edit_user.html', {'form': form})


def delete_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('user_detail')


def logout_view(request):
    logout(request)
    return redirect('login')
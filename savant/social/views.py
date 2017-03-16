from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})

@login_required
def index(request):
    return render(request, 'social/index.html', {})

@login_required
def profile(request):
    return render(request, 'social/profile.html', {})

@login_required
def math_list(request):
    users = User.objects.filter(groups__name='matematica')
    return render(request, 'social/matematica.html', {'users': users})

@login_required
def info_list(request):
    users = User.objects.filter(groups__name='informatica')
    return render(request, 'social/informatica.html', {'users': users})
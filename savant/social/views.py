from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})

@login_required
def index(request):
    return render(request, 'social/index.html', {})

@login_required
def profile(request, pk):
    profile_user = get_object_or_404(User, pk=pk)
    return render(request, 'social/profile.html', {'profile_user': profile_user})

@login_required
def math_list(request):
    users = User.objects.filter(groups__name='Matemática')
    return render(request, 'social/matematica.html', {'users': users})

@login_required
def info_list(request):
    users = User.objects.filter(groups__name='Informática')
    return render(request, 'social/informatica.html', {'users': users})
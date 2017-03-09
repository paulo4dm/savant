from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})

@login_required
def index(request):
    return render(request, 'social/index.html', {})
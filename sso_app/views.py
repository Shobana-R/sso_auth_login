from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'login.html')


def index(request):
    return HttpResponse("Hello, Welcome to Single Sign-on Authentication")

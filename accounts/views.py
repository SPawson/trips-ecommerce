from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate

from .forms import UserRegistrationForm

# Create your views here.

def register(request):
    """Register new users"""
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"user_form": form})
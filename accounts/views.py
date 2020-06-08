from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from checkout.models import OrderInformation, OrderLineItem
from itertools import chain
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

def login(request):
    """Allows the user to login and be authenticated"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout(request):
    """Logs the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))

@login_required
def profile(request):
    """Allows the user to see their profile and order history"""
    user = request.user
    user_orders = get_user_orders(user)
    line_items = get_order_lines(user)
    print(line_items)

    return render(request, 'profile.html', {'user':user, 'orders':user_orders, 'line_items': line_items})


def get_user_orders(user):
    """Returns a list of the users orders"""

    orders = OrderInformation.objects.filter(customer=user)



    return orders

def get_order_lines(user):
    """Returns a list of the users orders"""

    order_lines = OrderLineItem.objects.filter(order__customer=user)

    return order_lines


#Code snippets for login taken from CI authentication lesson
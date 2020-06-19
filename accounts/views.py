from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import auth, messages
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from checkout.models import OrderInformation, OrderLineItem
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    else:
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

    paginator = Paginator(user_orders, 3)
    page = request.GET.get('page')

    try:
        order_items = paginator.page(page)
    except PageNotAnInteger:
        order_items = paginator.page(1)
    except EmptyPage:
        order_items = paginator.page(paginator.num_pages)

    index = order_items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, 'profile.html', {'user': user,
                                            'orders': order_items,
                                            'line_items': line_items,
                                            'page_range': page_range})


def get_user_orders(user):
    """Returns a list of the users orders"""
    orders = OrderInformation.objects.filter(customer=user)
    return orders


def get_order_lines(user):
    """Returns a list of the users orders"""
    order_lines = OrderLineItem.objects.filter(order__customer=user)
    return order_lines


# Code snippets for login taken from CI authentication lesson

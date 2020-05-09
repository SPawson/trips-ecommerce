from django.shortcuts import render
from .models import Product

# Create your views here.

def return_products(request):
    """Returns the trips (products) to the user based
     upon their filter selections"""
    products = Product.objects.all()

    return render(request, "products.html", {'products': products})
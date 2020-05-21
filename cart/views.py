from django.shortcuts import redirect, render
from django.urls import reverse

#Code snippets taken from the Code Institute 'Ecommerce Lessons'

def add_to_cart(request, id):
    """Allows products to be added to the cart"""

    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def view_cart(request):
    """ Returns the cart view to the user"""

    return render(request, "cart-overview.html")
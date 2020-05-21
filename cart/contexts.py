from django.shortcuts import get_object_or_404
from products.models import Product

#Code snippet taken from the Code institures Ecommerce lesson

def is_valid_query(param):
    """Checks the query param for valid data"""
    return param != "" and param is not None

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0


    
    for id, quantity in cart.items():
        
        product = get_object_or_404(Product, pk=id)
        if is_valid_query(quantity) and is_valid_query(product.price):
            total += int(quantity) * product.price
            product_count += int(quantity)
            cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
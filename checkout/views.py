from django.shortcuts import get_object_or_404, redirect, render
from trips import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import OrderInformation, OrderLineItem
from .forms import OrderForm, MakePaymentForm
from products.models import Product 
from django.utils import timezone
from django.contrib import messages
import stripe
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """ Processes the cart objects and allows
    user to purchase goods
    """

    if request.method == 'POST':

        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid() and order_form.is_valid():
            print('valid form')
            order = order_form.save(commit=False)
            order.order_date = timezone.now()
            print(request.user.id)
            order.customer = request.user
            order.save()


            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(order = order,
                product = product, 
                quantity = quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100), # as it is in pence
                    currency = "gbp",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except:
                messages.error(request, "Your card was declined")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment at this time")
        else:
            messages.error(request, "We are unable to take a payment with that card")

    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        
    return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form })
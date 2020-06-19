from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from trips import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import OrderInformation, OrderLineItem
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from django.utils import timezone
from django.contrib import messages
import stripe
import json
from django.http import HttpResponseBadRequest
from django.urls import reverse


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """ Processes the cart objects and allows
    user to purchase goods - if there are no objects
    in the cart the user is redirected back to the store
    """
    cart = request.session.get('cart', {})
    print(cart)

    if cart != {}:

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

                total = 0
                for id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=id)
                    total += quantity * product.price
                    order_line_item = OrderLineItem(order=order,
                                                    product=product,
                                                    quantity=quantity)
                    order_line_item.save()

                print(total)

                saved_order = get_object_or_404(OrderInformation, pk=order.id)
                saved_order.order_total = total
                saved_order.save()

                customer = None

                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),  # as it is in pence
                        currency="gbp",
                        description=request.user.email,
                        card=payment_form.cleaned_data['stripe_id'],)
                except:
                    messages.error(request, "Your card was declined")

                if customer.paid:

                    request.session['cart'] = {}
                    response = {'url': '/'}
                    return HttpResponse(json.dumps(response),
                                        content_type='application/json')
                else:
                    messages.error(request,
                                   "Unable to take payment at this time")
                    response = {'stripe': 'error'}
                    return HttpResponseBadRequest(
                        json.dumps(response),
                        content_type='application/json')

            elif order_form.errors:
                return HttpResponseBadRequest(
                                              order_form.errors.as_json(),
                                              content_type='application/json')

        else:
            order_form = OrderForm()
            payment_form = MakePaymentForm()

        return render(request, 'checkout.html', {'order_form': order_form,
                                                 'payment_form': payment_form})

    else:
        return redirect(reverse('products'))

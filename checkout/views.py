from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'You have NO items in your cart')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KIdChHYTYZ8t0z67oQumiUihrq9bv5WNBMdpIDRiZrluIERl4vDRA04LAnrHNZ9GGsRmpzNNrzF5lGSFRp0ijz3009NpUvJFz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """ Makes the cart content available to all app templates """
    cart_items = []
    total = 0
    items_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        items_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.SHIPPING_FEE_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.SHIPPING_FEE_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = total + shipping

    context = {
        'cart_items': cart_items,
        'total': total,
        'items_count': items_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'shipping_fee_threshold': settings.SHIPPING_FEE_THRESHOLD,
        'grand_total': grand_total,
    }
    return context

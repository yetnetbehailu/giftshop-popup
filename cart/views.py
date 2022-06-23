from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def cart_view(request):
    """ View that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity off the selected item to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update the quantity of the specified item to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
    request.session['cart'] = cart

    return redirect(reverse('cart_view'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        request.session['cart'] = cart

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    View that displays all products including logic to sort & search \
    queries """
    products = Product.objects.filter(is_service=False)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def all_services(request):
    """ View that displays all of the services"""
    services = Product.objects.filter(is_service=True)

    context = {
        'services': services,
    }

    return render(request, 'products/services.html', context)

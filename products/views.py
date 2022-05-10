from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    """
    View that displays all products including logic to sort & search \
    queries """
    products = Product.objects.filter(is_service=False)
    # Displays none when hasn't been selected yet eg on page load
    categories = None
    sub_categories = None

    # Displays the selected category items
    if request.GET:
        if 'category' in request.GET:
            # splits existing categories into a list at the commas
            categories = request.GET['category'].split(',')
            # the __in syntax searches for the name field in category model
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sub_category' in request.GET:
            sub_categories = request.GET['sub_category']
            products = products.filter(sub_category=sub_categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def all_services(request):
    """ View that displays all of the services"""
    services = Product.objects.filter(is_service=True)

    context = {
        'services': services,
    }

    return render(request, 'products/services.html', context)

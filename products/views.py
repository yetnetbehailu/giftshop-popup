from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


def all_products(request):
    """
    View that displays all products including logic to sort & search \
    queries """
    products = Product.objects.filter(is_service=False)
    # Displays none when hasn't been selected yet eg on page load
    categories = None
    sub_categories = None
    query = None
    sort = None
    direction = None

    if request.GET:
        # Displays the selected category items
        if 'category' in request.GET:
            # splits existing categories into a list at the commas
            categories = request.GET['category'].split(',')
            # the __in syntax searches for the name field in category model
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sub_category' in request.GET:
            sub_categories = request.GET['sub_category']
            products = products.filter(sub_category=sub_categories)

        # Displays search form queries
        if 'q' in request.GET:
            query = request.GET['q']
            # if query blank display error message
            if not query:
                messages.error(request, 'No search quest entered!')
                return redirect(reverse('products'))
            # if query present enable search by name or description
            # the __i syntax makes the query case insensitive
            search_query = Q(name__icontains=query) | \
                Q(description__icontains=query)
            # To filter products according to quest pass query to filter method
            products = products.filter(search_query)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_categories': categories,
        'search_word': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View that specifically displays individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def all_services(request):
    """ View that displays all of the services"""
    services = Product.objects.filter(is_service=True)

    context = {
        'services': services,
    }

    return render(request, 'products/services.html', context)

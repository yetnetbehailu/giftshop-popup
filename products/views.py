from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Product, Category


def all_products(request):
    """
    View that displays all products including logic to sort & search \
    queries """
    products = Product.objects.filter(is_service=False).order_by('id')
    # Displays none when hasn't been selected yet eg on page load
    categories = None
    selected_sub_category = None
    sub_category_name = set()
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
            selected_sub_category = request.GET['sub_category']
            products = products.filter(sub_category=selected_sub_category)
            for product in products:
                sub_category_name.add(product.get_sub_category_display())
            # Cast set to a list then convert list to string object
            sub_category_name = ','.join(list(sub_category_name))

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

    # Pagination logic
    paginator = Paginator(products, 9)  # Show 9 products per page

    # Get request variable value if exsist else default to 1
    page_num = request.GET.get('page', 1)

    try:   # returns the desired page object
        product_page = paginator.page(page_num)
    except PageNotAnInteger:  # if page not an integer then default to 1
        product_page = paginator.page(1)
    except EmptyPage:  # if page is empty return the last page
        product_page = paginator.page(paginator.num_pages)

    context = {
        'products': product_page,
        'selected_categories': categories,
        'search_word': query,
        'current_sorting': current_sorting,
        'selected_sub_category': selected_sub_category,
        'sub_category_name': sub_category_name,
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

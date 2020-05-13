from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, Country

# Create your views here.


def is_valid_query(param):
    """Checks the query param for valid data"""
    return param != "" and param is not None

def return_categories():
    """Returns a list of categories for dropdown"""
    categories = Category.objects.all()

    return categories

def return_countries():
    """Returns a list of categories for dropdown"""
    countries = Country.objects.all()
    
    return countries

def return_products(request):
    """Returns the trips (products) to the user based
     upon their filter selections"""
   #categories = return_categories()
   
    name_or_location_contains_query = request.GET.get("name-or-location-contains")
    category_query = request.GET.get("category-filter")
    country_query = request.GET.get("country")
    sort_by_query = request.GET.get("sort-by")
    date_query = request.GET.get("datepicker")
    sort_by_value = 'start_date'

    if is_valid_query(sort_by_query):
        if sort_by_query=='price-high': sort_by_value='-price'
        if sort_by_query=='price-low': sort_by_value='price'
    
    products = Product.objects.all().order_by(sort_by_value)
    

    if is_valid_query(name_or_location_contains_query):
        products = products.filter(Q(name__icontains=name_or_location_contains_query)
         | Q(location__icontains=name_or_location_contains_query)).distinct().order_by(sort_by_value)
    
    if is_valid_query(category_query):
        products = products.filter(category=category_query).order_by(sort_by_value)
    
    if is_valid_query(country_query):
        products = products.filter(country=country_query).order_by(sort_by_value)
    
    if is_valid_query(date_query):
        products= products.filter(start_date__gte=date_query)
        
    pagination = Paginator(products, 1)
    page = request.GET.get('page')

    try:
        items = pagination.page(page)
    except PageNotAnInteger:
        items = pagination.page(1)
    except EmptyPage:
        items = pagination.page(pagination.num_pages)

    index = items.number -1
    max_index = len(pagination.page_range)
    start_index = index - 5 if index >=5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = pagination.page_range[start_index:end_index]

    context = {
        'items': items,
        'categories': return_categories(),
        'countries': return_countries(),
        'page_range': page_range,
    }

    return render(request, "products.html", context)


    
    
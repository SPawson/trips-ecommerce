from django.contrib import admin
from .models import Category, Product, Country

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Country)
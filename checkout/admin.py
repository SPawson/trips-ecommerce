from django.contrib import admin
from .models import OrderInformation, OrderLineItem

# Register your models here.
admin.site.register(OrderInformation)
admin.site.register(OrderLineItem)
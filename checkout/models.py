from django.db import models
from products.models import Product
from django.contrib.auth.models import User
import datetime

# Create your models here.


class OrderInformation(models.Model):
    """Stores users order information"""

    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    firstname = models.CharField(max_length=20, blank=False)
    lastname = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    address1 = models.CharField(max_length=40, blank=False)
    address2 = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    order_date = models.DateField(default=datetime.date.today, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.date, self.customer.username)


class OrderLineItem(models.Model):
    """Stores information about the individual order item"""
    order = models.ForeignKey(OrderInformation, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} x {1} @ {2}".format(self.product.name, self.quantity, self.product.price)

from django.db import models
from products.models import Product
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinLengthValidator

# Create your models here.


class OrderInformation(models.Model):
    """Stores users order information"""

    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    firstname = models.CharField(max_length=20, validators=[MinLengthValidator(2)] ,blank=False)
    lastname = models.CharField(max_length=20, validators=[MinLengthValidator(2)], blank=False)
    phone_number = models.CharField(max_length=15, validators=[MinLengthValidator(11)], blank=False)
    town_or_city = models.CharField(max_length=40, validators=[MinLengthValidator(2)], blank=False)
    address1 = models.CharField(max_length=40, validators=[MinLengthValidator(2)], blank=False)
    address2 = models.CharField(max_length=40, validators=[MinLengthValidator(2)], blank=False)
    postcode = models.CharField(max_length=10, validators=[MinLengthValidator(6)], blank=True)
    county = models.CharField(max_length=40, validators=[MinLengthValidator(2)], blank=False)
    country = models.CharField(max_length=40, validators=[MinLengthValidator(2)], blank=False)
    order_date = models.DateField(default=datetime.date.today, null=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    

    validatiors=[MinLengthValidator(2)]

    def __str__(self):
        return "OrderID:{0} Date:{1} Customer:{2}".format(self.id, self.order_date, self.customer.username)


class OrderLineItem(models.Model):
    """Stores information about the individual order item"""
    order = models.ForeignKey(OrderInformation, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "OrderID:{0} - {1} x {2} @ {3}".format(self.order.id, self.product.name, self.quantity, self.product.price)

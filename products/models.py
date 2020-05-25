from django.db import models
import datetime

class Category(models.Model):
    """Category model for the trips"""
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Country(models.Model):
    """Country model for trips"""
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    """Model used for the representing trips"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, default=None)
    country = models.ForeignKey(Country, default=None, on_delete=models.DO_NOTHING,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(default=None, blank=True, null=True)
    images = models.ImageField(upload_to='media/images')
    category = models.ForeignKey(Category, default=None, on_delete=models.DO_NOTHING,)
    latitude = models.DecimalField(max_digits=6, decimal_places=4, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=4, null=True)

    def __str__(self):
        return self.name
    
    def snippet(self):
        return self.description[:250] + "..."


class Comment(models.Model):
    """Model for product comments"""
    name = models.CharField(max_length=100)
    comment = models.TextField()
    post_date = models.DateField(null=True, default=datetime.date.today())
    product_id = models.ForeignKey(Product, default=None, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


from django.db import models
from accounts.models import User
from product.models import *
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_price = models.IntegerField(default=0, null=True, blank=True)
    product_final = models.IntegerField(default=0, null=True, blank=True)
    product_discount = models.IntegerField(default=0, null=True, blank=True)
    product_qty = models.IntegerField(default=0, null=True, blank=True)
    product_order_status = models.CharField(max_length=200, default='Pending', null=True, blank=True)
    product_payment_mode = models.CharField(max_length=200, default='', null=True, blank=True)
    product_payment_status = models.CharField(max_length=200, default='', null=True, blank=True)

    # Address
    name = models.CharField(max_length=100, default='', null=True, blank=True)
    email = models.EmailField(default='', null=True, blank=True)
    phone = models.CharField(max_length=10, default='', null=True, blank=True)
    alt_phone = models.CharField(max_length=10, default='', null=True, blank=True)
    location = models.CharField(max_length=100, default='', null=True, blank=True)
    house_no = models.CharField(max_length=100, default='', null=True, blank=True)
    road_name = models.CharField(max_length=100, default='', null=True, blank=True)
    landmark = models.CharField(max_length=100, default='', null=True, blank=True)
    city = models.CharField(max_length=100, default='', null=True, blank=True)
    state = models.CharField(max_length=100, default='', null=True, blank=True)
    pin = models.CharField(max_length=100, default='', null=True, blank=True)
    country = models.CharField(max_length=100, default='', null=True, blank=True)
    seller_name = models.CharField(max_length=200, default='', null=True, blank=True)
    seller_phone = models.CharField(max_length=10, default='', null=True, blank=True)
    date = models.CharField(max_length=50, default='', null=True, blank=True)
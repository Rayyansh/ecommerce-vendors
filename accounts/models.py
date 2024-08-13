from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default='', null=True, blank=True)
    company_name = models.CharField(max_length=100, default='', null=True, blank=True)
    company_slug = models.CharField(max_length=100, default='', null=True, blank=True)
    email = models.EmailField(default='', null=True, blank=True)
    pin = models.CharField(max_length=10, default='', null=True, blank=True)
    photo = models.FileField(upload_to="uploads", default='', null=True, blank=True)
    bank_name = models.CharField(max_length=100, default='', null=True, blank=True)
    account_holder_name = models.CharField(max_length=100, default='', null=True, blank=True)
    account_number = models.CharField(max_length=100, default='', null=True, blank=True)
    ifsc_code = models.CharField(max_length=100, default='', null=True, blank=True)

    address = models.CharField(max_length=100, default='', null=True, blank=True)
    state = models.CharField(max_length=100, default='', null=True, blank=True)
    city = models.CharField(max_length=100, default='', null=True, blank=True)
    gst = models.CharField(max_length=100, default='', null=True, blank=True)
    phone = models.CharField(max_length=10, default='', null=True, blank=True)

    gst_certificate = models.FileField(upload_to="uploads", default='', null=True, blank=True)
    udhyam_certificate = models.FileField(upload_to="uploads", default='', null=True, blank=True)
    pan_card = models.FileField(upload_to="uploads", default='', null=True, blank=True)
    cancelled_check = models.FileField(upload_to="uploads", default='', null=True, blank=True)
    other_document = models.FileField(upload_to="uploads", default='', null=True, blank=True)

    date = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    otp = models.IntegerField(default=9241, null=True, blank=True)
    verification = models.CharField(max_length=100, default='Done', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class BannerImage(models.Model):
    image = models.ImageField(upload_to="Banner_Image", default='', null=True, blank=True)


class Transaction(models.Model):
    TRANSACTION_STATUS_CHOICES = [
        ('INITIATED', 'Initiated'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed')
    ]

    transaction_id = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS_CHOICES, default='INITIATED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_id


class Support(models.Model):
    choice = ((0, "cataloging-pricing"), (1, "orders-delivery"), (2, "payments"), (3, "seller-shopping"), (4, "other"))
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, default='', null=True, blank=True)
    category = models.IntegerField(choices=choice, default=0, null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class Enquiry(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    interested=models.CharField(max_length=100)


class Ticket(models.Model):
    subject = models.CharField(max_length=190, default='', null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    image = models.ImageField(upload_to="Ticket", default='', null=True, blank=True)
    phone = models.CharField(max_length=10, default='', null=True, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=100, default='Open', null=True, blank=True)

    def __str__(self):
        return str(self.subject)
from django.db import models
from tinymce.models import HTMLField
from accounts.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='', null=True, blank=True)
    product_image1 = models.ImageField(upload_to="uploads", default='', null=True, blank=True)
    product_image2 = models.ImageField(upload_to="uploads", default='', null=True, blank=True)
    product_image3 = models.ImageField(upload_to="uploads", default='', null=True, blank=True)
    wholesale = models.CharField(max_length=100, default='', null=True, blank=True)
    maincategory = models.ForeignKey('Maincategory', on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)
    unit = models.CharField(max_length=200, default='', null=True, blank=True)
    weight = models.CharField(max_length=200, default='', null=True, blank=True)
    minimum_purchase_qty = models.IntegerField(default=1, null=True, blank=True)
    tags = models.TextField(default='', null=True, blank=True)
    product_thumbnail = models.ImageField(upload_to="uploads", default='', null=True, blank=True)
    link_type = models.CharField(max_length=200, default='', null=True, blank=True)
    video_link = models.CharField(max_length=200, default='', null=True, blank=True)
    color = models.CharField(max_length=200, default='', null=True, blank=True)
    attribute = models.CharField(max_length=200, default='', null=True, blank=True)
    unit_price = models.FloatField(default=0, null=True, blank=True)
    discount_range = models.CharField(max_length=200, default='', null=True, blank=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)
    qty = models.IntegerField(default=1, null=True, blank=True)
    sku = models.CharField(max_length=200, default='', null=True, blank=True)
    # Wholesale Details
    wholesale_min_qty1 = models.IntegerField(default=0, null=True, blank=True)
    wholesale_max_qty1 = models.IntegerField(default=0, null=True, blank=True)
    wholesale_price1 = models.FloatField(default=0.0, null=True, blank=True)

    wholesale_min_qty2 = models.IntegerField(default=0, null=True, blank=True)
    wholesale_max_qty2 = models.IntegerField(default=0, null=True, blank=True)
    wholesale_price2 = models.FloatField(default=0.0, null=True, blank=True)

    wholesale_min_qty3 = models.IntegerField(default=0, null=True, blank=True)
    wholesale_max_qty3 = models.IntegerField(default=0, null=True, blank=True)
    wholesale_price3 = models.FloatField(default=0.0, null=True, blank=True)

    wholesale_min_qty4 = models.IntegerField(default=0, null=True, blank=True)
    wholesale_price4 = models.FloatField(default=0.0, null=True, blank=True)

    specification_name = models.TextField(null=True, blank=True)
    specification_value = models.TextField(null=True, blank=True)
    # End Wholesale Details
    external_link = models.CharField(max_length=200, default='', null=True, blank=True)
    external_link_button_text = models.CharField(max_length=200, default='', null=True, blank=True)
    key_features = HTMLField(default='', null=True, blank=True)
    subcategory_specification = HTMLField(default='', null=True, blank=True)
    product_description = HTMLField(default='', null=True, blank=True)
    product_faq_title = models.TextField(default='', null=True, blank=True)
    product_faq_answer = models.TextField(default='', null=True, blank=True)
    pdf_specification = models.CharField(max_length=200, default='', null=True, blank=True)
    seo_meta_title = models.TextField(default='', null=True, blank=True)
    meta_description = models.TextField(default='', null=True, blank=True)
    meta_image = models.ImageField(upload_to="uploads", default='', null=True, blank=True)
    free_shipping = models.CharField(max_length=200, default='', null=True, blank=True)
    fat_rate = models.CharField(max_length=200, default='', null=True, blank=True)
    is_product_quality_multiply = models.CharField(max_length=200, default='', null=True, blank=True)
    low_stock_qty = models.CharField(max_length=200, default='', null=True, blank=True)
    hide_stock = models.CharField(max_length=200, default='', null=True, blank=True)
    cash_on_delivery = models.CharField(max_length=200, default='', null=True, blank=True)
    shipping_day = models.CharField(max_length=200, default='', null=True, blank=True)
    tax = models.CharField(max_length=200, default='', null=True, blank=True)

    supercategory = models.CharField(max_length=200, default='', null=True, blank=True)
    verification = models.CharField(max_length=100, default='Pending', null=True, blank=True)

    featured = models.BooleanField(default=False, null=True, blank=True)
    best_selling = models.BooleanField(default=False, null=True, blank=True)
    upcoming = models.BooleanField(default=False, null=True, blank=True)

    slug = models.SlugField

    def __str__(self):
        return str(self.id) + "-- " + str(self.name)


class Slider(models.Model):
    image1=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image2=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image3=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image4=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image5=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image6=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image7=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image8=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image9=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image10=models.ImageField(upload_to="uploads",default='',null=True,blank=True)


class Maincategory(models.Model):
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image1=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image2=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image3=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image4=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image5=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image6=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image7=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image8=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image9=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image10=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    title=models.CharField(max_length=400,default='',null=True,blank=True)
    description=models.CharField(max_length=1000,default='',null=True,blank=True)

    slug = models.SlugField()

    def __str__(self):
        return self.name


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    maincategory=models.ForeignKey(Maincategory, on_delete=models.CASCADE, null=True, blank=True)
    category_name=models.CharField(max_length=100,default='',null=True,blank=True)
    category_specification=HTMLField(default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image1=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image2=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image3=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image4=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image5=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image6=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image7=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image8=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image9=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    image10=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    title=models.CharField(max_length=400,default='',null=True,blank=True)
    description=models.CharField(max_length=1000,default='',null=True,blank=True)

    slug = models.SlugField()
    def __str__(self):
        return str(self.category_name)

class Brand(models.Model):
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    title=models.CharField(max_length=400,default='',null=True,blank=True)
    description=models.CharField(max_length=1000,default='',null=True,blank=True)

    slug = models.SlugField
    def __str__(self):
        return str(self.name)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_rating = models.CharField(max_length=10, default='', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    customer_comment = models.TextField(default='', null=True, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=100, default='Pending', null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Wishlist(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_image=models.ImageField(upload_to="Product-Image",default='',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.product.name)
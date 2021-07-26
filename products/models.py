from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.expressions import Value
from django.db.models.fields.related import ForeignKey
from accounts.models import CustomUser

class MainCategory(models.Model):
    value = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    value = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    value = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    value = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    value = models.CharField(max_length=50)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size

class Color(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):

    product_name = models.CharField(max_length=200)
    main_category = models.ForeignKey(MainCategory, on_delete=DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=DO_NOTHING)
    brand_name = models.ForeignKey(Brand, on_delete=DO_NOTHING)
    model_number = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField()
    specification = models.TextField()
    product_size = models.CharField(max_length=100, blank=True)
    min_order_quantity = models.IntegerField()
    quantity_unit = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    min_quantity = models.CharField(max_length=100)
    max_quantity = models.CharField(max_length=100)
    product_pic = models.ImageField(null=True)

    # price_2 = models.CharField(max_length=100, blank=True, null=True)
    # min_quantity_2 = models.CharField(max_length=100, blank=True, null=True)
    # max_quantity_2 = models.CharField(max_length=100, blank=True, null=True)

    # price_3 = models.CharField(max_length=100, blank=True, null=True)
    # min_quantity_3 = models.CharField(max_length=100, blank=True, null=True)
    # max_quantity_3 = models.CharField(max_length=100, blank=True, null=True)

    # price_4 = models.CharField(max_length=100, blank=True, null=True)
    # min_quantity_4 = models.CharField(max_length=100, blank=True, null=True)
    # max_quantity_4 = models.CharField(max_length=100, blank=True, null=True)

    # price_5 = models.CharField(max_length=100, blank=True, null=True)
    # min_quantity_5 = models.CharField(max_length=100, blank=True, null=True)
    # max_quantity_5 = models.CharField(max_length=100, blank=True, null=True)

    # add photo / colour and gallery photos

    in_stock = models.BooleanField()
    date_added = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class ProductGallery(models.Model):
    image = models.ImageField()
    product = ForeignKey(Product, on_delete=models.CASCADE)
    color = ForeignKey(Color, on_delete=models.DO_NOTHING, blank=True, null=True)

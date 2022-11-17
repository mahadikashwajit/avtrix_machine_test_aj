from django.db import models

# Create your models here.

class Product(models.Model):
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    unit_price = models.CharField(max_length=255)
    order_date = models.CharField(max_length=255)

    class Meta:
        db_table = "products"




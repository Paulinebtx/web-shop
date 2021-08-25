from django.db import models
from django.urls import reverse
from webshop.models import product
from authenticationuser.models import Customer

# Create your models here.
class basket(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

    # date_order = models.DateTimeField(auto_now_add=True)
    # complete = models.BooleanField(default=False)


    def _str_(self):
        return self.title


class basket_elem(models.Model):
    # quantity = models.IntegerField()
    basket = models.ForeignKey(basket, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    # date_add = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.product.title
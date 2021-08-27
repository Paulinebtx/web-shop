from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField()
    image = models.URLField(max_length=255, blank = True, null = True)

    # delete a product by say if it's active or not
    # is_active = models.BooleanField(default=True)


    def _str_(self):
        return self.title

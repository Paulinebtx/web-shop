from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()

    def _str_(self):
        return self.title

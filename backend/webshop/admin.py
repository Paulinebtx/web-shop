from django.contrib import admin
from .models import product

class webshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'image')
# Register your models here.
admin.site.register(product, webshopAdmin)
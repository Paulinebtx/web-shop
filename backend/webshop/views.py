

# Create your views here.
# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import webshopSerializer
from .models import product

# Create your views here.

class webshopView(viewsets.ModelViewSet):
    serializer_class = webshopSerializer
    queryset = product.objects.all()



# def register(response):
#     return render()

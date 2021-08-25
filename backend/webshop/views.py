

# Create your views here.
# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import webshopSerializer
from .models import Product

class webshopView(viewsets.ModelViewSet):
    serializer_class = webshopSerializer
    queryset = Product.objects.all()



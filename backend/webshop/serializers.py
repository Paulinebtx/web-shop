from rest_framework import serializers
from .models import product

class webshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('id', 'title', 'description', 'price', 'image')
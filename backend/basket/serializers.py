from rest_framework import serializers
from .models import basket
from .models import basket_elem

class basketSerializer(serializers.ModelSerializer):
    class Meta:
        model = basket
        fields = ('__all__')
       
       
class basket_elemSerializer(serializers.ModelSerializer):
    class Meta:
        model = basket_elem
        fields = ('__all__')
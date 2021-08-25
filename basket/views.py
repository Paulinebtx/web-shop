from rest_framework import viewsets
from .serializers import basketSerializer
from .serializers import basket_elemSerializer
from .models import basket
from .models import basket_elem

class BasketView(viewsets.ModelViewSet):
    serializer_class = basketSerializer
    queryset = basket.objects.all()

class Basket_elemView(viewsets.ModelViewSet):
    serializer_class = basket_elemSerializer
    queryset = basket_elem.objects.all()
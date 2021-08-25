  
"""backend URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from webshop import views as webshop_views
from authenticationuser import views as customer_views
from basket import views as basket_views
from basket import views as basket_elem_views
# from authenticationuser.views import signupView



router = routers.DefaultRouter()
router.register(r'webshops', webshop_views.webshopView, 'webshop')
router.register(r'customer', customer_views.CustomerView, 'customer')
router.register(r'baskets', basket_views.BasketView, 'basket')
router.register(r'basketItems', basket_elem_views.Basket_elemView, 'basketItem')


urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('api/', include(router.urls)),
  
]
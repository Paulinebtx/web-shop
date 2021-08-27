from django.urls import include, path
from .views import user,login_view
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('user', user, name='user'),
    path('login',login_view,name='login'),
]
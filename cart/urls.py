from django.urls import path
from .views import create_cart_item
urlpatterns=[
  path('<slug:slug>',create_cart_item,name='cart_item'),
]
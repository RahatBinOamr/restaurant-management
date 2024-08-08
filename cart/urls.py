from django.urls import path
from .views import create_cart_item,view_cart_item,increment_quantity,decrement_quantity,delete_cart_item
urlpatterns=[
  path('cart-item/',view_cart_item,name='cart'),
  path('<slug:slug>/',create_cart_item,name='cart_item'),
  path('increment/<int:pk>/', increment_quantity, name='increment'),
  path('decrement/<int:pk>/', decrement_quantity, name='decrement'),
  path('delete/<int:pk>/', delete_cart_item, name='delete'),
]
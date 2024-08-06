from django.urls import path
from .views import dinner_item,lunch_item,break_fist_item,items_page,item_detail

urlpatterns =[
  path('items',items_page,name='items'),
  path('break-first/', break_fist_item, name='break-first'),
  path('lunch/', lunch_item, name='lunch'),
  path('dinner/',dinner_item, name='dinner'),
  path('<slug:slug>',item_detail,name='detail'),
]
from django.urls import path
from .views import create_order_contact_submit,order_information,update_order_info


urlpatterns =[
  path("order_contact_form",create_order_contact_submit,name='order_contact_form'),
  path("order_information",order_information,name='order_info'),
  path("update/<int:pk>",update_order_info,name='update_order_info')
]
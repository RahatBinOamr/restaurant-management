from django.urls import path
from .views import create_order_contact_submit,order_information, order_summary, order_summary_pdf,update_order_info, user_orders


urlpatterns =[
  path("order_contact_form",create_order_contact_submit,name='order_contact_form'),
  path("order_information",order_information,name='order_info'),
  path("update/<int:pk>",update_order_info,name='update_order_info'),
  path('order/data/', user_orders, name='user_orders'),
  path('order/<int:order_id>/', order_summary, name='order_summary'),
  path('order/<int:order_id>/pdf/', order_summary_pdf, name='order_summary_pdf'),
]
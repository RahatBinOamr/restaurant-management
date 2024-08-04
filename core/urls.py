from django.urls import path
from .views import home_page,about_page,service_page,contact_page,team_page,testimonial_page,booking_page,items_page,subscription_page
urlpatterns =[
  path('',home_page,name='home'),
  path('items',items_page,name='items'),
  path('contact/',contact_page,name='contact'),
  path('about/',about_page,name='about'),
  path('service/', service_page, name='service'),
  path('team/', team_page, name='team'),
  path('testimonial/', testimonial_page, name='testimonial'),
  path('booking/', booking_page, name='booking'),
  path('subscription/', subscription_page, name='subscription'),
]
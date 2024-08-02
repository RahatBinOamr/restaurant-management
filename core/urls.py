from django.urls import path
from .views import home_page,about_page,service_page,contact_page,team_page,testimonial_page
urlpatterns =[
  path('',home_page,name='home'),
  path('contact/',contact_page,name='contact'),
  path('about/',about_page,name='about'),
  path('service/', service_page, name='service'),
  path('team/', team_page, name='team'),
  path('testimonial/', testimonial_page, name='testimonial'),
]
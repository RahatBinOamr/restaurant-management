from django.shortcuts import render
from .models import Contact
from django.contrib import messages
# Create your views here.
def home_page(request):
  return render(request, 'index.html')
def items_page(request):
  return render(request, 'items.html')

def about_page(request):
  return render(request, 'about.html')

def service_page(request):
  return render(request, 'service.html')

def contact_page(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    Contact.objects.create(name=name, email=email, subject=subject, message=message)
    messages.success(request, 'Your message send successfully!!!')
  return render(request, 'contact.html')

def team_page(request):
  return render(request, 'team.html')

def testimonial_page(request):
  return render(request,'testimonial.html')

def booking_page(request):
  return render(request, 'booking.html')
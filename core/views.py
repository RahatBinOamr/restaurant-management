from django.shortcuts import render
from .models import Contact,Reservation
from django.contrib import messages
from datetime import datetime
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
    if request.method == 'POST':
        name = request.POST.get('b-name')
        email = request.POST.get('b-email')
        dateTime = request.POST.get('b-datetime')
        people = request.POST.get('b-people')
        special_requests = request.POST.get('b-special_requests')

        # Convert dateTime to the correct format
        try:
            dateTime = datetime.strptime(dateTime, "%m/%d/%Y %I:%M %p")
        except ValueError:
            messages.error(request, "Invalid date and time format.")
            return render(request, 'booking.html')

        Reservation.objects.create(
            name=name,
            email=email,
            special_request=special_requests,
            people=people,
            datetime=dateTime
        )
        messages.success(request, f"Your table booking was successfully on {dateTime} for {people} person(s).")
    return render(request, 'booking.html')
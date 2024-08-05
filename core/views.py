from django.http import HttpResponseRedirect
from django.shortcuts import render

from core.forms import SubscribeForm
from .models import Contact,Reservation
from django.contrib import messages
from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from menue.models import Item

# Create your views here.
def home_page(request):
  items = Item.objects.all().order_by('?')[:14]

  context ={
     'items': items
  }
  return render(request, 'index.html',context)




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

        # Create the reservation
        Reservation.objects.create(
            name=name,
            email=email,
            special_request=special_requests,
            people=people,
            datetime=dateTime
        )

        # Send a confirmation email
        subject = 'Booking Confirmation'
        message = f"Dear {name},\n\nYour table booking was successfully made for {dateTime.strftime('%B %d, %Y at %I:%M %p')} for {people} person(s)."

        smtp_server = smtplib.SMTP('smtp-relay.brevo.com', 587)
        smtp_server.starttls()
        smtp_server.login("6e87d6002@smtp-brevo.com", "j8Wadh0ZvX7CR9kx")

        msg = MIMEMultipart()
        msg['From'] = "rahatbinomar@gmail.com"
        msg['To'] = email 
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'html'))
        smtp_server.quit()

        # Add a success message
        messages.success(request, f"Your table booking was successfully made for {dateTime.strftime('%B %d, %Y at %I:%M %p')} for {people} person(s).")
        
    return render(request, 'booking.html')


def subscription_page(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            subject = 'Subscription Successful'
            message = f'Thank you {subscription.email} for subscribing to restaurant site!'
            smtp_server = smtplib.SMTP('smtp-relay.brevo.com', 587)
            smtp_server.starttls()
            smtp_server.login("6e87d6002@smtp-brevo.com", "j8Wadh0ZvX7CR9kx")

            msg = MIMEMultipart()
            msg['From'] = "rahatbinomar@gmail.com"
            msg['To'] = subscription.email 
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'html'))
            smtp_server.quit()
            messages.success(request, 'You are subscribed successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    
from django.shortcuts import render

# Create your views here.
def home_page(request):
  return render(request, 'index.html')


def about_page(request):
  return render(request, 'about.html')

def service_page(request):
  return render(request, 'service.html')

def contact_page(request):
  return render(request, 'contact.html')

def team_page(request):
  return render(request, 'team.html')

def testimonial_page(request):
  return render(request,'testimonial.html')

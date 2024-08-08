from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Item,Review
from django.contrib import messages
# Create your views here.
def items_page(request):
  items = Item.objects.all().order_by('?')[:14]

  context ={
     'items': items
  }
  return render(request, 'items.html',context)


def lunch_item(request):
  lunch = Item.objects.filter(period='LUNCH')
  context ={
    'items':lunch
  }
  return render(request, 'lunch.html', context)

def dinner_item(request):
  dinner = Item.objects.filter(period='DINNER')
  context ={
    'items':dinner
  }
  return render(request, 'dinner.html', context)

def break_fist_item(request):
  break_first = Item.objects.filter(period='BREAK_FIST')
  context ={
    'items':break_first
  }
  return render(request, 'break_fist.html', context)


def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    related_item = Item.objects.filter(period=item.period).exclude(slug=item.slug)
    show_reviews = Review.objects.filter(item=item)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating', None)
        message = request.POST.get('message')
        Review.objects.create(name=name, email=email, rating=rating, message=message, item=item)
        messages.success(request, 'Your review added successfully!!!')
        return redirect(request.path)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        offset = int(request.GET.get('offset', 0))
        limit = 4
        reviews = show_reviews[offset:offset + limit]
        reviews_data = [{'name': review.name, 'rating': review.rating, 'message': review.message} for review in reviews]
        return JsonResponse(reviews_data, safe=False)
    context = {
        'item': item,
        'items': related_item,
        'reviews': show_reviews[:4]  # Initially show 4 reviews
    }
    return render(request, 'item_detail.html', context)




from django.shortcuts import render
from .models import Item
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



def item_detail(request,slug):
  item = Item.objects.get(slug=slug)
  related_item = Item.objects.filter(period=item.period).exclude(slug=item.slug)
  context ={
    'item':item,
    'items':related_item
  }
  return render(request, 'item_detail.html', context)
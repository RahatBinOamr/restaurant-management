from django.http import HttpResponseRedirect
from .models import CartItem
from menue.models import Item
from django.contrib import messages
# Create your views here.

def create_cart_item(request, slug):
    item = Item.objects.get(slug=slug)
    session_key = request.session.session_key

    if not session_key:
        request.session.create() 
        session_key = request.session.session_key
    existing_cart_item = CartItem.objects.filter(item=item, session_key=session_key).first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
        messages.success(request, 'Item quantity updated successfully')
    else:
        CartItem.objects.create(item=item, session_key=session_key, quantity=1)
        messages.success(request, 'Item added to cart successfully')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



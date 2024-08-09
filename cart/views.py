from django.http import HttpResponseRedirect
from .models import CartItem,Cart
from menue.models import Item
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
# Create your views here.

def create_cart_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
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


def view_cart_item(request):
    session_key = request.session.session_key
    if session_key:
        cart_items = CartItem.objects.filter(session_key=session_key)
        cart_data = Cart.objects.filter(items__in=cart_items).distinct().first()
        if cart_data is None:
            cart_data = Cart.objects.create()
            cart_data.items.set(cart_items)  
        context = {
            'cart_items': cart_items,
            'cart_data': cart_data
        }
        return render(request, 'cart_items.html', context)
    



def increment_quantity(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.quantity += 1
    item.save()
    messages.success(request, 'Item Increment successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def decrement_quantity(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        messages.success(request, 'Item decremented successfully!')
    else:
        item.delete()
        messages.success(request, 'Item removed from cart!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_cart_item(request,pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.delete()
    messages.success(request, 'Item removed from cart!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
from django.shortcuts import render,redirect
from django.contrib import messages

from cart.models import Cart, CartItem
from .models  import OrderContactInfo
# Create your views here.



def create_order_contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('o_name')
        email = request.POST.get('o_email')
        phone = request.POST.get('o_phone')
        address = request.POST.get('o_address')
        session_key = request.session.session_key

        # Check if an OrderContactInfo entry exists for the current session
        existing_info = OrderContactInfo.objects.filter(session_key=session_key)
        if existing_info.exists():
            existing_info.delete()  
        
        OrderContactInfo.objects.create(name=name, email=email, phone=phone, address=address, session_key=session_key)
        messages.success(request, 'Order contact info submitted successfully!!')
        return redirect('order_info')

    return render(request, 'order_contact_form.html')



def order_information(request):
  session_key = request.session.session_key
  if session_key:
        order_contact_info = OrderContactInfo.objects.get(session_key = session_key)
        cart_items = CartItem.objects.filter(session_key=session_key)
        cart_data = Cart.objects.filter(items__in=cart_items).distinct().first()
        context ={
          'order_contact_info':order_contact_info,
          'items':cart_items,
          'cart_data':cart_data
        }
        return render(request,'order_info.html',context)
  

def update_order_info(request, pk):
    contact = OrderContactInfo.objects.get(pk=pk)
    session_key = request.session.session_key
    if request.method == 'POST':
        name = request.POST.get('u_name')
        email = request.POST.get('u_email')
        phone = request.POST.get('u_phone')
        address = request.POST.get('u_address')
        session_key = request.session.session_key

        # Update the fields of the contact instance
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.address = address
        contact.session_key = session_key

        contact.save()
        messages.success(request, 'Order contact information updated successfully')
        return redirect('order_info')

    context = {
        'contact': contact,
    }
    return render(request, 'update_info.html', context)

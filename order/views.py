from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from cart.models import Cart, CartItem
from .models  import Order, OrderContactInfo
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
    cart_items = CartItem.objects.filter(session_key=session_key)
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
        'cart_items':cart_items
    }
    return render(request, 'update_info.html', context)


def user_orders(request):
    session_key = request.session.session_key
    orders = Order.objects.filter(session_key=session_key).order_by('-created_at')

    return render(request, 'user_orders.html', {'orders': orders})


def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_summary.html', {'order': order})


def order_summary_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html_string = render_to_string('order_summary_pdf.html', {'order': order})
    
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order_id}.pdf"'
    return response
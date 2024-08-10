from django.shortcuts import redirect
from order.models import Order, OrderContactInfo
import stripe
from django.conf import settings
from django.views import View
from cart.models import Cart
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(id=self.kwargs["pk"])
        session_key = request.session.session_key

        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        if settings.DEBUG:
            domain = "http://127.0.0.1:8000/"
        else:
            domain = "https://your-production-domain.com"

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Your Cart Total',
                        },
                        'unit_amount': int(cart.grand_total * 100),  
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + 'payment/success/',
            cancel_url=domain + 'payment/cancel/',
            client_reference_id=session_key,  
            metadata={
                "session_key": session_key,  
                "cart_id": cart.id,
            },
        )
        return redirect(checkout_session.url)
    

class SuccessView(TemplateView):
    template_name = "success.html"
 
class CancelView(TemplateView):
    template_name = "cancel.html"



@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
 
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)
 
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        payment_intent = session["payment_intent"]
        
        # Assuming you are storing session_key in client_reference_id or metadata
        session_key = session.get("client_reference_id") or session.get("metadata", {}).get("session_key")

        if not session_key:
            print("Session key not found in Stripe session.")
            return HttpResponse(status=400)

        try:
            contact_info = OrderContactInfo.objects.get(session_key=session_key)
        except OrderContactInfo.DoesNotExist:
            print(f"No contact info found for session key: {session_key}")
            return HttpResponse(status=404)

        try:
            cart = Cart.objects.filter(items__session_key=session_key).order_by('-id').first()
        except Cart.DoesNotExist:
            print(f"No cart found for session key: {session_key}")
            return HttpResponse(status=404)

        # Create the Order object
        order = Order.objects.create(
            contact_info=contact_info,
            cart=cart,
            status='processed',  
            session_key=session_key
        )

        print(f"Order created: {order}")

    return HttpResponse(status=200)
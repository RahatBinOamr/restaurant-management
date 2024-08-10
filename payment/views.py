from django.shortcuts import redirect
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
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        else:
            domain = "https://your-production-domain.com"

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd ',
                        'product_data': {
                            'name': 'Your Cart Total',
                        },
                        'unit_amount': cart.grand_total * 100,  
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
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
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
 
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        payment_intent = session["payment_intent"]
 
        # TODO - send an email to the customer
 
    return HttpResponse(status=200)
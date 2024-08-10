from django.urls import path
from .views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,stripe_webhook
)
 
urlpatterns = [
    path('payment/cancel/', CancelView.as_view(), name='cancel'),
    path('payment/success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
]
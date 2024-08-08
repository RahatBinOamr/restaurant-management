from django import template
from cart.models import CartItem

register = template.Library()

@register.simple_tag
def cart_count(request, user):
    guest_user_count = 0

    guest_user_count = CartItem.objects.filter(session_key=request.session.session_key).count()
    
    total_count = guest_user_count 
    
    return total_count if total_count > 0 else 0
from django.db import models

from cart.models import Cart

# Create your models here.
class OrderContactInfo(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone = models.CharField(max_length=20)
  address = models.TextField()
  session_key = models.CharField(max_length=200, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}-{self.email}-{self.phone}-{self.address}"
  


class Order(models.Model):
    contact_info = models.ForeignKey(OrderContactInfo, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    session_key = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.order_total is None:
            self.order_total = self.cart.grand_total
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order #{self.id} - {self.contact_info.name}'
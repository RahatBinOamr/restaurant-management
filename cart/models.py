from django.db import models
from menue.models import Item
from django.db.models import Sum

# Create your models here.

class CartItem(models.Model):
  item = models.ForeignKey(Item,on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)

  @property
  def item_price(self):
        return self.item.price
  @property
  def total_price(self):
        return self.item_price * self.quantity
  
  def __str__(self):
        return f'{self.item.name} x {self.quantity}'
  

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)

    @property
    def grand_total(self):
        return self.items.aggregate(total=Sum('total_price'))['total'] or 0
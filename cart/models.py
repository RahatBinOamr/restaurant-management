from django.db import models
from menue.models import Item
from django.db.models import Sum,F

# Create your models here.

class CartItem(models.Model):
      item = models.ForeignKey(Item,on_delete=models.CASCADE)
      quantity = models.PositiveIntegerField(default=1)
      session_key = models.CharField(max_length=200, blank=True, null=True)


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
    shipping_cost = models.PositiveIntegerField(default=20)

    @property
    def total_items_price(self):
        return self.items.annotate(total_price=F('quantity') * F('item__price')).aggregate(total=Sum('total_price'))['total'] or 0

    @property
    def grand_total(self):
        return self.total_items_price + self.shipping_cost

    def __str__(self):
        return f'Cart with {self.items.count()} items - Total: {self.grand_total}'
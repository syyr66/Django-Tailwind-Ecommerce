from django.db import models
from products.models import Product

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_total_price(self):
        return sum([i.get_total_price() for i in self.items.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
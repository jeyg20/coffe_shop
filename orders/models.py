from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order {self.id} by {self.user}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.order} - {self.quantity} {self.product}"

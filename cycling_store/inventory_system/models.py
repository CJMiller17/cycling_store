from django.db import migrations, models
from django.utils import timezone 
# Create your models here.

class Inventory(models.Model):
    item = models.TextField(blank=True)
    in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item}: {self.in_stock} in stock"
    
class Customer(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} "
    
class Order(models.Model):
    date = models.DateField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True)
    qty = models.PositiveIntegerField(default=1)
    paid = models.BooleanField(default=False)

    def __str__(self):
        item_display = self.item.item if self.item else "Deleted Item"
        return f"{self.id:05d} {self.customer} bought  x{self.qty} {item_display} on {self.date}. Paid?: {self.paid}" 
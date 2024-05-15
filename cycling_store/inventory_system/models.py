from django.db import migrations, models
from django.utils import timezone 
# Create your models here.

class Transport(models.Model):
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
    item = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} bought a {self.item} on {self.date}. Paid?: {self.paid}" 
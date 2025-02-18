from django.db import models
from django.utils import timezone

# Models
class Supplier(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name

    def __str__(self):
        return(f"{self.getName()} - {self.city}, {self.country} created at: {self.created_at}")

class WaterBottle(models.Model):
    sku = models.CharField(max_length = 3, unique=True) # SKU = Stock Keeping Unit
    brand = models.CharField(max_length = 300)
    cost = models.DecimalField(max_digits = 6, decimal_places = 2)
    size = models.CharField(max_length = 30)
    mouth_size = models.CharField(max_length = 30)
    color = models.CharField(max_length = 30)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.PositiveIntegerField()

    def __str__(self):
        return(f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplied_by.getName()}, {self.cost} : {self.current_quantity}")
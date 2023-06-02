from django.db import models

from branches.models import Branch
from cars.models import Car
from customer.models import Customer


# Create your models here.
class Rent(models.Model):
    car_plate = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_RG = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch_cnpj = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateField()
    finishes_at = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

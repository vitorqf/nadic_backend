from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    surname = models.CharField(max_length=100,null=True)
    RG = models.CharField(max_length=20,null=True, unique=True)
    address_street = models.CharField(max_length=100,null=True)
    address_number = models.IntegerField(null=True)
    address_neighborhood = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Customers"

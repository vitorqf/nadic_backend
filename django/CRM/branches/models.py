from django.db import models
from django.db.models import Sum


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=14, null=True, unique=True)
    address_street = models.CharField(max_length=100, null=True)
    address_number = models.IntegerField(null=True)
    address_neighborhood = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.cnpj

    def total_rented_cars(self):
        from cars.models import Car

        return self.car_set.filter(status=Car.UNAVAILABLE).count()

    def total_rent_prices(self):
        from cars.models import Car

        rented_cars = self.car_set.filter(status=Car.UNAVAILABLE)
        total = (
            rented_cars.annotate(rent_price=Sum("rent__price"))
            .values("rent_price")
            .aggregate(total=Sum("rent_price"))["total"]
        )
        return total if total is not None else 0

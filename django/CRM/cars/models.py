from django.db import models

from branches.models import Branch


# Create your models here.
class Car(models.Model):
    AVAILABLE = 1
    UNAVAILABLE = 2

    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable"),
    )

    model = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    color = models.CharField(max_length=100, null=True)
    plate = models.CharField(max_length=8, null=True, unique=True)
    chassis_type = models.CharField(max_length=20, null=True)
    status = models.PositiveSmallIntegerField(
        null=True, default=1, choices=STATUS_CHOICES
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="cars", null=True)

    def __str__(self):
        return self.plate

    class Meta:
        verbose_name_plural = "Cars"

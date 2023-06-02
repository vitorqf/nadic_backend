from django.db import models


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
    status = models.CharField(
        max_length=20, null=True, default=AVAILABLE, choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = "Cars"

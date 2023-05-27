from django.db import models


# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100,null=True)
    brand = models.CharField(max_length=100,null=True)
    year = models.IntegerField(null=True)
    color = models.CharField(max_length=100,null=True)
    plate = models.CharField(max_length=7,null=True)
    chassis_type = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name_plural = "Cars"
from rest_framework import viewsets

from cars.api.serializers import CarSerializer
from cars.models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

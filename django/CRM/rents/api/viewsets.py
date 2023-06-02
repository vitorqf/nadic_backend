from rest_framework import viewsets

from rents.api.serializers import RentSerializer
from rents.models import Rent


class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

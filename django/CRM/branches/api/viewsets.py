from rest_framework import viewsets

from branches.api.serializers import BranchSerializer
from branches.models import Branch


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

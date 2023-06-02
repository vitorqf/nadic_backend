from django.db.models import Sum
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from branches.api.serializers import BranchSerializer
from branches.models import Branch


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    @permission_classes([IsAdminUser])
    def rent_total(self, request):
        rent_total = Branch.objects.aggregate(total=Sum("rent__price"))

        return Response({"all_branches_total_rent": rent_total["total"]})

    @permission_classes([IsAdminUser])
    def rent_total_by_branch(self, request, pk):
        rent_total = Branch.objects.filter(pk=pk).aggregate(total=Sum("rent__price"))

        return Response({"branch_total_rent": rent_total["total"]})

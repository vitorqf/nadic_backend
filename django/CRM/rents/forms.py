from django import forms

from branches.models import Branch
from cars.models import Car
from customer.models import Customer

from .models import Rent


class RentForm(forms.ModelForm):
    car_plate = forms.ModelChoiceField(
        queryset=Car.objects.all(),
        label="Car Plate",
        widget=forms.Select(attrs={"class": "select select-bordered w-full max-w-xs"}),
    )
    customer_RG = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        label="Customer RG",
        widget=forms.Select(attrs={"class": "select select-bordered w-full max-w-xs"}),
    )
    branch_cnpj = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        label="Branch CNPJ",
        widget=forms.Select(attrs={"class": "select select-bordered w-full max-w-xs"}),
    )
    created_at = forms.DateTimeField(
        label="Created At",
        widget=forms.DateTimeInput(
            attrs={"class": "input input-bordered w-full max-w-xs"}
        ),
    )
    finishes_at = forms.DateTimeField(
        label="Finishes At",
        widget=forms.DateTimeInput(
            attrs={"class": "input input-bordered w-full max-w-xs"}
        ),
    )
    price = forms.DecimalField(
        label="Price",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={"class": "input input-bordered w-full max-w-xs"}
        ),
    )

    class Meta:
        model = Rent
        fields = "__all__"

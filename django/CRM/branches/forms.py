from django import forms

from .models import Branch


class BranchForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
    )
    cnpj = forms.CharField(
        label="CNPJ",
        max_length=18,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
    )
    address_street = forms.CharField(
        label="Address Street",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
    )
    address_number = forms.IntegerField(
        label="Address Number",
        widget=forms.NumberInput(
            attrs={"class": "input input-bordered w-full max-w-xs"}
        ),
    )
    address_neighborhood = forms.CharField(
        label="Address Neighborhood",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
    )

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get("cnpj")

        cnpj = "".join(filter(str.isdigit, cnpj))

        if len(cnpj) != 14:
            raise forms.ValidationError("CNPJ must have 14 digits.")

        return cnpj

    def save_branch(self):
        cnpj = self.clean_cnpj()
        branch = Branch(cnpj=cnpj)
        branch.name = self.cleaned_data["name"]
        branch.address_street = self.cleaned_data["address_street"]
        branch.address_number = self.cleaned_data["address_number"]
        branch.address_neighborhood = self.cleaned_data["address_neighborhood"]
        branch.save()

    def update_branch(self, branch):
        cnpj = self.clean_cnpj()
        branch.cnpj = cnpj
        branch.name = self.cleaned_data["name"]
        branch.address_street = self.cleaned_data["address_street"]
        branch.address_number = self.cleaned_data["address_number"]
        branch.address_neighborhood = self.cleaned_data["address_neighborhood"]
        branch.save()

    class Meta:
        model = Branch
        fields = "__all__"

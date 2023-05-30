from django.core.validators import RegexValidator

from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100,null=True, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    surname = forms.CharField(label='Surname', max_length=100,null=True, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    RG = forms.CharField(label='RG', validators=[RegexValidator(r'^\d{1,2}[.]?\d{3}[.]?\d{3}[-]?\d{1}$', 'Customer RG is invalid.')], max_length=20,null=True, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    address_street = forms.CharField(label='Address Street', max_length=100,null=True, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    address_number = forms.IntegerField(label='Address Number',null=True, widget=forms.NumberInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    address_neighborhood = forms.CharField(label='Address Neighborhood', max_length=100,null=True, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    
    def clean_rg(self):
        rg = self.cleaned_data.get('RG')

        rg = ''.join(filter(str.isdigit, rg))

        if len(rg) != 9:
            raise forms.ValidationError('RG must have 9 digits.')
        
        return rg
    
    def save_customer(self):
        rg = self.cleaned_data['RG']
        rg = self.clean_rg(rg)
        customer = Customer(rg=rg)
        customer.name = self.cleaned_data['name']
        customer.surname = self.cleaned_data['surname']
        customer.address_street = self.cleaned_data['address_street']
        customer.address_number = self.cleaned_data['address_number']
        customer.address_neighborhood = self.cleaned_data['address_neighborhood']
        customer.save()
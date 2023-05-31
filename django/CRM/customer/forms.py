from django.core.validators import RegexValidator

from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    surname = forms.CharField(label='Surname', max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    RG = forms.CharField(label='RG', max_length=20, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    address_street = forms.CharField(label='Address Street', max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    address_number = forms.IntegerField(label='Address Number', widget=forms.NumberInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    address_neighborhood = forms.CharField(label='Address Neighborhood', max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    
    def clean_rg(self):
        rg = self.cleaned_data.get('RG')

        rg = ''.join(filter(str.isdigit, rg))

        if len(rg) != 9:
            raise forms.ValidationError('RG must have 9 digits.')
        
        return rg
    
    def save_customer(self):
        rg = self.clean_rg()
        customer = Customer(RG=rg)
        customer.name = self.cleaned_data['name']
        customer.surname = self.cleaned_data['surname']
        customer.address_street = self.cleaned_data['address_street']
        customer.address_number = self.cleaned_data['address_number']
        customer.address_neighborhood = self.cleaned_data['address_neighborhood']
        customer.save()
        
    def update_customer(self, customer):
        rg = self.clean_rg()
        customer.RG = rg
        customer.name = self.cleaned_data['name']
        customer.surname = self.cleaned_data['surname']
        customer.address_street = self.cleaned_data['address_street']
        customer.address_number = self.cleaned_data['address_number']
        customer.address_neighborhood = self.cleaned_data['address_neighborhood']
        customer.save()
        
    class Meta:
        model = Customer
        fields = '__all__'
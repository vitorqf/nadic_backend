from django.core.validators import RegexValidator

from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    model = forms.CharField(label='Model', max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    brand = forms.CharField(label='Brand', max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    year = forms.IntegerField(label='Year', widget=forms.NumberInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    color = forms.CharField(label='Color', max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    plate = forms.CharField(validators=[
            RegexValidator(
                regex=r'^([A-Za-z]{3}[-]?\d{4})|([A-Za-z]{4}[-]?\d{3})$',
                message='Plate must be with format AAA9999, AAAA999, AAA-9999 or AAAA-999',
                code='invalid_plate'
            )
        ], label='Plate', max_length=8, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    chassis_type = forms.CharField(label='Chassis Type', max_length=20, widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1900 or year > 2100:
            raise forms.ValidationError('Year must be >= 1900 or <= 2100.')
        return year
    
    def save_car(self):
        plate = self.cleaned_data['plate'].replace('-', '')
        car = Car(plate=plate.upper())
        car.save()
    
    class Meta:
        model = Car
        fields = '__all__'
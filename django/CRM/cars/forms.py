from django import forms
from django.core.validators import RegexValidator

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "model": forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
            "brand": forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
            "year": forms.NumberInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
            "color": forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
            "plate": forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
            "chassis_type": forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
            "image": forms.FileInput(attrs={"class": "input input-bordered w-full max-w-xs"}),
        }
        labels = {
            "model": "Model",
            "brand": "Brand",
            "year": "Year",
            "color": "Color",
            "plate": "Plate",
            "chassis_type": "Chassis Type",
            "image": "Image",
        }
        error_messages = {
            "year": {"invalid": "Year must be between 1900 and 2100."},
            "plate": {
                "invalid": "Plate must be with format AAA9999, AAAA999, AAA-9999 or AAAA-999."
            },
        }

    def clean_year(self):
        year = self.cleaned_data.get("year")
        if not 1900 <= year <= 2100:
            raise forms.ValidationError("Year must be between 1900 and 2100.")
        return year

    def save_car(self):
        plate = self.cleaned_data["plate"].replace("-", "")
        car = Car(
            plate=plate.upper(),
            model=self.cleaned_data["model"],
            brand=self.cleaned_data["brand"],
            year=self.cleaned_data["year"],
            color=self.cleaned_data["color"],
            chassis_type=self.cleaned_data["chassis_type"],
            branch=self.cleaned_data["branch"],
        )
        image_file = self.cleaned_data["image"]
        if image_file:
            car.image.save(image_file.name, image_file)
        car.save()

    def update_car(self, car):
        plate = self.cleaned_data["plate"].replace("-", "")
        car.plate = plate.upper()
        car.model = self.cleaned_data["model"]
        car.brand = self.cleaned_data["brand"]
        car.year = self.cleaned_data["year"]
        car.color = self.cleaned_data["color"]
        car.chassis_type = self.cleaned_data["chassis_type"]
        car.branch = self.cleaned_data["branch"]
        car.save()
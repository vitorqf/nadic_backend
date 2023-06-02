from django.shortcuts import get_object_or_404, redirect, render

from cars.models import Car
from rents.forms import RentForm
from rents.models import Rent


# Create your views here.
def create_rent(request):
    if request.method == "POST":
        form = RentForm(request.POST)
        if form.is_valid():
            rent = form.save()

            car = get_object_or_404(Car, plate=rent.car_plate)
            car.status = 2
            car.save()

            return redirect("list_rents")

    else:
        form = RentForm()

    form.fields["car_plate"].queryset = Car.objects.filter(status=Car.AVAILABLE)

    return render(request, "create_rent.html", {"form": form})


def delete_rent_by_id(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)

    car = get_object_or_404(Car, plate=rent.car_plate)
    car.status = 1
    car.save()

    rent.delete()
    return redirect("list_rents")


def list_rents(request):
    rents = Rent.objects.all()
    return render(request, "list_rents.html", {"rents": rents})


def edit_rent_by_id(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)

    if request.method == "POST":
        form = RentForm(request.POST, instance=rent)
        if form.is_valid():
            form.save()
            return redirect("list_rents")
    else:
        form = RentForm(instance=rent)

    return render(request, "edit_rent.html", {"form": form})


def get_rent_by_id(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)
    return render(request, "rent_by_id.html", {"rent": rent})

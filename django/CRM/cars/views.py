from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from .forms import CarForm
from .models import Car


def list_cars(request):
    cars = Car.objects.all()
    return render(request, "list_cars.html", {"cars": cars})

def get_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        return render(request, "home.html", {"car": car})
    
    except Car.DoesNotExist:
        return HttpResponse("Car not found")

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            try:
                form.save_car()
                return JsonResponse({"message": "Success", 'car': form.cleaned_data})
            
            except IntegrityError:
                return JsonResponse({"message": "Plate already exists"})
        
    else:
        form = CarForm()

    return render(request, 'create_car.html', {'form': form})

def edit_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        if request.method == 'POST':
            form = CarForm(request.POST, instance=car)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "Car updated successfully", 'car': form.cleaned_data})
        
        else:
            form = CarForm(instance=car)

        return render(request, 'edit_car.html', {'form': form, 'car': car})
    
    except Car.DoesNotExist:
        return HttpResponse("Car not found")
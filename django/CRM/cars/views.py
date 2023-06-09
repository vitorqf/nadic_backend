from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .forms import CarForm
from .models import Car


def list_cars(request):
    cars = Car.objects.all()
    return render(request, "list_cars.html", {"cars": cars})

def get_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        return render(request, "car_by_id.html", {"car": car})
    
    except Car.DoesNotExist:
        return HttpResponse("Car not found")

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            try:
                form.save_car()
                return redirect('list_cars') 
            
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
                form.update_car(car=car)
                return redirect('list_cars') 
        
        else:
            form = CarForm(instance=car)

        return render(request, 'edit_car.html', {'form': form, 'car': car})
    
    except Car.DoesNotExist:
        return HttpResponse("Car not found")
    
def delete_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        car.delete()
        return redirect('list_cars') 
    
    except Car.DoesNotExist:
        return HttpResponse("Car not found")
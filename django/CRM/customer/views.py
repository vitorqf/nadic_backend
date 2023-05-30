from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from MySQLdb import IntegrityError

from .forms import CustomerForm
from .models import Customer


# Create your views here.
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "list_customers.html", {"customers": customers})


def get_customer_by_id(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        return render(request, "home.html", {"customer": customer})
    
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found")
    
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save_customer()
                return JsonResponse({"message": "Success", 'customer': form.cleaned_data})
            
            except IntegrityError:
                return JsonResponse({"message": "RG already exists"})
        
    else:
        form = CustomerForm()

    return render(request, 'create_customer.html', {'form': form})

def delete_customer_by_id(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return JsonResponse({"message": "Success"})
    
    except Customer.DoesNotExist:
        return JsonResponse({"message": "Customer not found"})
    

def edit_customer_by_id(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                try:
                    form.save_customer()
                    return JsonResponse({"message": "Success", 'customer': form.cleaned_data})
                
                except IntegrityError:
                    return JsonResponse({"message": "RG already exists"})
            
        else:
            form = CustomerForm()
    
        return render(request, 'edit_customer.html', {'form': form, 'customer': customer})
    
    except Customer.DoesNotExist:
        return JsonResponse({"message": "Customer not found"})
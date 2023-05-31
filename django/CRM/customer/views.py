from django.forms import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
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
        return render(request, "customer_by_id.html", {"customer": customer})
    
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found")
    
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save_customer()
                return redirect('list_customers')
            
            except IntegrityError:
                return HttpResponse("RG already exists")
        
    else:
        form = CustomerForm()

    return render(request, 'create_customer.html', {'form': form})

def delete_customer_by_id(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        return redirect('list_customers')
    
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found")
    

def edit_customer_by_id(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        if request.method == 'POST':
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                    form.update_customer(customer=customer)
                    return redirect('list_customers') 
                
        
        else:
            form = CustomerForm(instance=customer)

        return render(request, 'edit_customer.html', {'form': form, 'customer': customer})
    
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found")
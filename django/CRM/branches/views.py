from django.forms import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from MySQLdb import IntegrityError

from .forms import BranchForm
from .models import Branches


# Create your views here.
def list_branches(request):
    branches = Branches.objects.all()
    return render(request, "list_branches.html", {"branches": branches})


def get_branch_by_id(request, branch_id):
    try:
        branch = Branches.objects.get(id=branch_id)
        return render(request, "branch_by_id.html", {"branch": branch})
    
    except Branches.DoesNotExist:
        return HttpResponse("Branches not found")
    
def create_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            try:
                form.save_branch()
                return redirect('list_branches')
            
            except IntegrityError:
                return HttpResponse("RG already exists")
        
    else:
        form = BranchForm()

    return render(request, 'create_branch.html', {'form': form})

def delete_branch_by_id(request, branch_id):
    try:
        branch = Branches.objects.get(id=branch_id)
        branch.delete()
        return redirect('list_branches')
    
    except Branches.DoesNotExist:
        return HttpResponse("Branches not found")
    

def edit_branch_by_id(request, branch_id):
    try:
        branch = Branches.objects.get(id=branch_id)
        if request.method == 'POST':
            form = BranchForm(request.POST, instance=branch)
            if form.is_valid():
                    form.update_branch(branch=branch)
                    return redirect('list_branches') 
                
        
        else:
            form = BranchForm(instance=branch)

        return render(request, 'edit_branch.html', {'form': form, 'branch': branch})
    
    except Branches.DoesNotExist:
        return HttpResponse("Branches not found")
from django.shortcuts import render,redirect
from superadmin.models import Vehicles
from django.shortcuts import get_object_or_404
from superadmin.forms import VehicleForm
from django.contrib.auth.decorators import login_required
# custom decorator 
from admins.decorator import admin_role_check
# Create your views here.
@admin_role_check
@login_required
def admin_home(request):
    return render(request,'admin_home.html')

@admin_role_check
@login_required   
def vehicle_list(request):
    vehicles = Vehicles.objects.all()
    context = {
        'vehicles': vehicles,
    }
    return render(request,'vehicle_admin_list.html',context)
    
@admin_role_check   
@login_required    
def vehicle_edit_admin(request,id):
    vehicle = get_object_or_404(Vehicles,id=id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vehicle_list_admin')
            
    context = {
        'form': form,
    
    }
    
    return render(request,'edit_vehicle.html',context)
    
@admin_role_check
@login_required    
def vehicle_view(request,id):
    vehicle = get_object_or_404(Vehicles,id=id)
    context = {
        'vehicle': vehicle,
    }
    return render(request,'vehicle_view.html',context)

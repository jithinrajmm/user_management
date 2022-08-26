from django.shortcuts import render
from django.shortcuts import get_object_or_404
from superadmin.models import Vehicles
from django.contrib.auth.decorators import login_required
# custom decorator
from users.decorator import user_role_check

# veiw start here 
@user_role_check
@login_required
def user_home(request):
    return render(request,'user_home.html')

@user_role_check
@login_required   
def user_list_vehicle(request):
    vehicles = Vehicles.objects.all()
    context = {
        
        'vehicles': vehicles,
    }
    return render(request,'user_vehicle_list.html',context)

@user_role_check   
@login_required    
def user_view_vehicle(request,id):
    vehicle = get_object_or_404(Vehicles,id=id)
    
    context = {
        'vehicle': vehicle,
    }
    return render(request,'user_view_vehicle.html',context)
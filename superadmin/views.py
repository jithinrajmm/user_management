from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import F
# models
from accounts.models import Account
from superadmin.models import Vehicles
# forms
from superadmin.forms import VehicleForm
# url 
from django.urls import reverse_lazy
# flash messages
from django.contrib import messages
# decorator usage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# custom decorator
from superadmin.decorator import super_admin_role
# THIS DECORATOR USED TO CHECK THE SUPER_ADMIN PERMISSION'S


@login_required
@super_admin_role
def super_admin_home(request):
    return render(request,'spr_home/index.html')

# #################################################################################
# USER MANAGEMENT
@method_decorator([login_required,super_admin_role],name='dispatch')   
class UserList(ListView):
    '''For listing the all users '''
    model = Account
    template_name = 'spr_home/user.html'
    context_object_name = 'users'
        
@method_decorator([login_required,super_admin_role],name='dispatch')    
class AdminRequest(ListView):
    '''For listing the all users '''
    model = Account
    template_name = 'spr_home/admin.html'
    context_object_name = 'admins'
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_admins=False,role='admin')
        return qs
        
@method_decorator([login_required,super_admin_role],name='dispatch')        
class AdminPermission(View):
    ''' For giving the permissions to the admins '''
    def get(self,*args,**kwargs):
        user_id = kwargs.get('user_id')
        user = Account.objects.get(id=user_id)
        user.is_admins = not user.is_admins
        user.save()
        return redirect('admin_request')
        
# #################################################################################
# VEHICLE MAMANGEMENT   
@method_decorator([login_required,super_admin_role],name='dispatch')        
class VehicleList(ListView):
    ''' for listing all the vehicles '''
    model = Vehicles
    template_name= 'spr_home/vehicle_list.html'
    context_object_name = 'vehicles'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['details'] =  False
        return context
        
@method_decorator([login_required,super_admin_role],name='dispatch')   
class CreateVehicle(CreateView):
    ''' For adding the vehicle '''
    model = Vehicles
    form_class = VehicleForm
    template_name = 'spr_home/create_vehicle.html'
    success_url =reverse_lazy('vehicle_list')
    
@method_decorator([login_required,super_admin_role],name='dispatch')    
class UpdateVehicle(UpdateView):
    ''' for updating the Vehicle '''
    model = Vehicles
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('vehicle_list')
    template_name = 'spr_home/create_vehicle.html'
    form_class = VehicleForm
    
    def form_valid(self,form):
        messages.success(self.request,'updated success fully')
        return super().form_valid(form)
        
@method_decorator([login_required,super_admin_role],name='dispatch')        
class DeleteVehicle(SuccessMessageMixin,DeleteView):
    'FOR DELETING THE VEHICLE RECORD'
    model = Vehicles
    success_url = reverse_lazy('vehicle_list')
    template_name = 'spr_home/confirm.html'
    success_message = "Deleted successfully."
    
    def delete(self,request,*args,**kwargs):
        messages.success(self.request,self.success_message)
        return super(DeleteVehicle,self).delete(request,*args,**kwargs)
        
@method_decorator([login_required,super_admin_role],name='dispatch')        
class VehicleDetail(DetailView):
    model = Vehicles
    template_name= 'spr_home/detail.html'
    context_object_name = 'single_vehicle'
    

    
        
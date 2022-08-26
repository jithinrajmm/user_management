from django.urls import path
from superadmin import views


urlpatterns = [ 
  path('',views.super_admin_home,name='super_admin_home'),
  path('userlist/',views.UserList.as_view(),name='userlist'),
#admin
  path('admin_request/',views.AdminRequest.as_view(),name='admin_request'),
  path('admin_permission/<int:user_id>/',views.AdminPermission.as_view(),name='admin_permission'),
  path('admin_permission/<int:user_id>/',views.AdminPermission.as_view(),name='admin_permission'),
#vehicle management
  path('vehicle_list/',views.VehicleList.as_view(),name='vehicle_list'),
  path('create_vehicle/',views.CreateVehicle.as_view(),name='create_vehicle'),
  path('update_vehicle/<int:pk>/',views.UpdateVehicle.as_view(),name='update_vehicle'),
  path('delete_vehicle/<int:pk>/',views.DeleteVehicle.as_view(),name='delete_vehicle'),
  path('vehicle_detail/<int:pk>/',views.VehicleDetail.as_view(),name='vehicle_detail'),
  

  
   
]
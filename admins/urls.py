from django.urls import path
from admins import views


urlpatterns = [
    path('',views.admin_home,name= 'admin_home'),
    path('vehicle_list_admin/',views.vehicle_list,name= 'vehicle_list_admin'),
    path('vehicle_edit_admin/<int:id>/',views.vehicle_edit_admin,name= 'vehicle_edit_admin'),
    path('vehicle_view/<int:id>/',views.vehicle_view,name= 'vehicle_view'),
    
    
]
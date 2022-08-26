from django.urls import path
from users import views

urlpatterns = [
    path('',views.user_home,name='user_home'),
    path('user_list_vehicle/',views.user_list_vehicle,name='user_list_vehicle'),
    path('user_view_vehicle/<int:id>/',views.user_view_vehicle,name='user_view_vehicle'),
    
]
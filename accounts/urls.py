from django.urls import path
from accounts import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('log_out/',views.user_logout,name='log_out'),
    path('user_registration/',views.user_registration,name='user_registration'),
]
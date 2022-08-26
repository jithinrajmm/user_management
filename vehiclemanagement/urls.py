"""vehiclemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from vehiclemanagement.views import all_home,not_allowed
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # for the homes
    path('',all_home,name='home'),
    # login user
    path('accounts/',include('accounts.urls')),
    # admin
    path('admins/',include('admins.urls')),
    # super admin
    path('super_admin/',include('superadmin.urls')),
    # user
    path('user/',include('users.urls')), 
    # not allowed
    path('not_allowed/',not_allowed,name='not_allowed'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

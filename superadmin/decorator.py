from django.shortcuts import redirect

def super_admin_role(view):
    def role_check(request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('home')
        else:       
            if request.user.is_superadmin:
                return view(request,*args,**kwargs)
            else:
                return redirect('not_allowed')
    return role_check
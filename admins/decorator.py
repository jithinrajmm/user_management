from django.shortcuts import redirect

def admin_role_check(view):
    def role_check(request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('home')
        else:       
            if request.user.role == 'admin' and request.user.is_admins:
                return view(request,*args,**kwargs)
            else:
                return redirect('not_allowed')
    return role_check
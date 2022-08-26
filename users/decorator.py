from django.shortcuts import redirect

def user_role_check(view):
    def role_check(request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('home')
        else:       
            if request.user.role == 'user' and request.user.is_user:
                return view(request,*args,**kwargs)
            else:
                return redirect('not_allowed')
    return role_check
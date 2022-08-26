from django.shortcuts import render,redirect
# forms
from django.contrib.auth.forms import AuthenticationForm
# custom forms
from accounts.forms import CustomUserCreationForm
# authentications
from django.contrib.auth import authenticate,login,logout
# flash messages 
from django.contrib import messages 

# for login user
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    forms = AuthenticationForm()
    if request.method == 'POST':
        forms = AuthenticationForm(request,data = request.POST)
        print(forms.errors)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            
            if user is not None:
                if user.role == 'admin' and user.is_admins == False:
                    messages.error(request, "Please contact to Admin For verification")
                    return redirect('home')
                else:
                    if user.role == 'admin' and user.is_admins:
                        login(request,user)
                        return redirect('admin_home')
                    elif user.role == 'user' and user.is_user:
                        login(request,user)
                        return redirect('user_home')
                    elif user.is_superadmin:
                        login(request,user)
                        return redirect('super_admin_home')
                    else:
                        messages.error(request,'Not valid user')
            else:
                messages.error(request,'Not valid information')
            
    context = {
      'form': forms,  
    }
    return render(request,'login/login.html',context)
    
def user_registration(request):
    # adding all users
    form = CustomUserCreationForm()
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = True
            
            if new_user.role == 'admin':
                new_user.save()
                return redirect('login') 
                        
            elif new_user.role == 'user':
                new_user.is_user = True
                new_user.save()
                return redirect('login')
                
    context = {
        'form': form,
    }            
    return render(request,'login/register.html',context)
def user_logout(request):
    ''' logout view of the user ,'''
    logout(request)
    return redirect('home')
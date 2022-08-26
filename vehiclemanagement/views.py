from django.shortcuts import render,redirect



def all_home(request):
    return render(request,'home/index.html')
      
def not_allowed(request):
    # for not allowed users on each role
    return render(request,'home/not_allowed.html')
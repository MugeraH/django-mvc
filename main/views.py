from django.shortcuts import render,reverse,redirect,get_object_or_404


import sys
sys.path.append("..")
from users.models import User

def LandingPageView(request):
    return render(request,'main/landing.html')

def HomePageView(request):
    return render(request,'main/home.html')

def AdminPageView(request):
    if request.user.is_superuser:
        return redirect('authentication:superuser_page')
        
    if not request.user.is_admin and not request.user.is_superuser:
        return redirect('main:user_page')
    
    return render(request,'main/admin_page.html')


def SuperUserPageView(request):
    if request.user.is_admin:
        return redirect('authentication:admin_page')
        
    if not request.user.is_admin and not request.user.is_superuser:
        return redirect('authentication:user_page')
    
    return render(request,'main/super_admin_page.html')

# Only users should see this page
def UserPageView(request):
    if request.user.is_superuser:
        return redirect('authentication:superuser_page')
        
    if  request.user.is_admin and not request.user.is_superuser:
        return redirect('authentication:admin_page')
    
    return render(request,'main/user_page.html')


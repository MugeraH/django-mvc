from django.shortcuts import render


import sys
sys.path.append("..")
from users.models import User

def LandingPageView(request):
    return render(request,'main/landing.html')

def HomePageView(request):
    return render(request,'main/home.html')


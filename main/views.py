from django.shortcuts import render


import sys
sys.path.append("..")
from users.models import User

def HomePageView(request):
    return render(request,'assets/home.html')


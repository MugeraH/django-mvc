from django import urls
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers


from . import views
from .views import HomePageView


app_name="authentication"

urlpatterns = [
     path('home',HomePageView,name='home'),
]


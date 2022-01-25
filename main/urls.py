from django import urls
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers


from . import views
from .views import HomePageView,LandingPageView,SuperUserPageView,AdminPageView,UserPageView


app_name="authentication"

urlpatterns = [
    path('',LandingPageView,name='landing'),
    path('home',HomePageView,name='home'),
    path('superuser',SuperUserPageView,name='superuser_page'),
    path('admin_page',AdminPageView,name='admin_page'),
    path('user',UserPageView,name='user_page'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

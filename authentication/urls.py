from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
    
    )
from users.views import SignupView
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('signup/',SignupView,name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
    
 
]

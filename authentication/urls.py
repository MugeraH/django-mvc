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

urlpatterns = [
    path('admin/', admin.site.urls),
]

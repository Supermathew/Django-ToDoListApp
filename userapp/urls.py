
from django.urls import path
from weather_app import views
from django.contrib.auth import views as auth_view
from userapp import views

urlpatterns = [
    path("login", auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout", auth_view.LogoutView.as_view(template_name='index.html'), name="logout"),
    path("register", views.register, name="register"),
    ]



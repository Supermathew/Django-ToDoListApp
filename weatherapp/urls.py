
from django.urls import path,include
from weather_app import views
from userapp import urls
from django.contrib import admin
from weather_app import views as todolist_views

urlpatterns = [
    
    path('todolist/',include('weather_app.urls')),
    path('admin/', admin.site.urls),
    path('account/',include('userapp.urls')),
    path('',todolist_views.indexpage,name='indexpage'),
    path('contact', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name='about'),
    # path("about/", views.about, name="about"),
    ]


from django.urls import path
from weather_app import views

urlpatterns = [
    path('',views.home,name='todolist'),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("taskupdate/<task_id>", views.taskupdate, name="taskupdate"),
    path("taskfalse/<task_id>", views.taskfalse, name="taskfalse"),
    path("tasktrue/<task_id>", views.tasktrue, name="tasktrue"),
    path("deletetask/<task_id>", views.deletetask, name="deletetask"),
    # path("message/",views.message,name="message"),

    # path("about/", views.about, name="about"),
    ]

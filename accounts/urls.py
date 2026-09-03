from django.urls import path
from . import views

urlpatterns = [

    path("doctor/login/", views.doctor_login, name="doctor_login"),
    path("patient/login/", views.patient_login, name="patient_login"),
    path("register/", views.register, name="register"),

]
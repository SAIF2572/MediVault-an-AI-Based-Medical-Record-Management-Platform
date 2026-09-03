from django.urls import path
from . import views

urlpatterns = [

    # path("register/<int:doctor_id>/", views.patient_register, name="patient_register"),

    path("doctor/search/", views.doctor_search, name="doctor_search"),

    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path("success/", views.patient_success, name="patient_success"),

]
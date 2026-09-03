from django.urls import path
from . import views

urlpatterns = [

    path("list/", views.hospital_list, name="hospital_list"),

    path("<int:hospital_id>/departments/", views.department_list, name="department_list"),

    path("department/<int:department_id>/doctors/", views.doctor_list, name="doctor_list"),

]
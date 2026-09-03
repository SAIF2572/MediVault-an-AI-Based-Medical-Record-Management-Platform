from django.shortcuts import render, get_object_or_404
from .models import Hospital, Department, Doctor


def hospital_list(request):

    hospitals = Hospital.objects.all()

    return render(request, "hospital_list.html", {
        "hospitals": hospitals
    })


def department_list(request, hospital_id):

    hospital = get_object_or_404(Hospital, id=hospital_id)

    departments = Department.objects.filter(hospital=hospital)

    return render(request, "department_list.html", {
        "hospital": hospital,
        "departments": departments
    })


def doctor_list(request, department_id):

    department = get_object_or_404(Department, id=department_id)

    doctors = Doctor.objects.filter(department=department)

    return render(request, "doctor_list.html", {
        "department": department,
        "doctors": doctors
    })
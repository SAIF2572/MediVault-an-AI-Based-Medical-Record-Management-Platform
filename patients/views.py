from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient
from hospitals.models import Doctor


def home(request):
    return render(request, "home.html")


@login_required
def doctor_search(request):

    patient = None
    reports = None

    total_patients = Patient.objects.count()

    from reports.models import Report
    total_reports = Report.objects.count()

    if request.method == "POST":

        uhid = request.POST.get("uhid")

        patient = Patient.objects.filter(uhid=uhid).first()

        if patient:
            reports = patient.reports.all()

    return render(request, "doctor_search.html", {

        "patient": patient,
        "reports": reports,
        "total_patients": total_patients,
        "total_reports": total_reports

    })


# Patient Registration with Doctor
def patient_register(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        age = request.POST.get("age")
        gender = request.POST.get("gender")

        patient = Patient.objects.filter(
            name=name,
            age=age,
            gender=gender,
            phone=phone
        ).first()

        if not patient:
            patient = Patient.objects.create(
                name=name,
                phone=phone,
                age=age,
                gender=gender,
                doctor=doctor
            )

        return render(request, "patient_success.html", {"patient": patient})

    return render(request, "patient_register.html", {"doctor": doctor})

from reports.models import Report

def patient_dashboard(request):

    uhid = request.POST.get("uhid") or request.GET.get("uhid")

    patient = None
    reports = []

    if uhid:
        patient = Patient.objects.filter(uhid=uhid).first()
        if patient:
            reports = Report.objects.filter(patient=patient)

    return render(request, "patient_dashboard.html", {
        "patient": patient,
        "reports": reports
    })

def patient_success(request):

    patient_id = request.GET.get("patient_id")

    patient = None

    if patient_id:
        patient = Patient.objects.filter(id=patient_id).first()

    return render(request, "patient_success.html", {
        "patient": patient
    })

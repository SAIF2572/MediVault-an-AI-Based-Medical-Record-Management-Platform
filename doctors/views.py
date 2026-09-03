from django.shortcuts import render, redirect
from patients.models import Patient
from reports.models import Report

def doctor_dashboard(request):

    uhid = request.GET.get("uhid")
    patient = None
    reports = []

    # POST = remark save
    if request.method == "POST":
        report_id = request.POST.get("report_id")
        remark = request.POST.get("remark")

        report = Report.objects.get(id=report_id)
        report.doctor_remark = remark
        report.save()

        return redirect(f"/doctor/search/?uhid={report.patient.uhid}")

    # GET = search
    if uhid:
        patient = Patient.objects.filter(uhid=uhid).first()
        if patient:
            reports = Report.objects.filter(patient=patient)

    return render(request, "doctor_dashboard.html", {
        "patient": patient,
        "reports": reports
    })
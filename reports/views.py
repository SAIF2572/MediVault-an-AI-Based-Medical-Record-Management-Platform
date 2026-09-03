from django.shortcuts import render,get_object_or_404
from patients.models import Patient
from .models import Report
from django.contrib import messages
from .ai_utils import analyze_report

def detect_report(filename):

    name = filename.lower()

    if "blood" in name:
        return "Blood Test","Blood report detected. Check hemoglobin and RBC levels."

    elif "ecg" in name:
        return "ECG","Electrocardiogram report for heart activity."

    elif "mri" in name:
        return "MRI","Magnetic resonance imaging scan report."

    elif "ct" in name:
        return "CT Scan","Computed tomography imaging report."

    else:
        return "General","General medical report."

def lab_upload(request):

    if request.method == "POST":

        uhid = request.POST.get("uhid")
        report_file = request.FILES.get("report_file")

        patient = Patient.objects.filter(uhid=uhid).first()

        if patient and report_file:
            #here only using file name
            text = report_file.name
            category, summary = analyze_report(text)

            Report.objects.create(
                patient=patient,
                report_file=report_file,
                report_type=category,
                ai_category=category,
                ai_summary=summary
            )

            messages.success(request, "Report uploaded successfully!")

        else:
            messages.error(request, "Invalid UHID or file missing!")

    return render(request, "lab_upload.html")

def view_report(request, report_id):

    report = get_object_or_404(Report, id=report_id)

    return render(request, "report_view.html", {"report": report})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Report

def add_remark(request, report_id):

    report = get_object_or_404(Report, id=report_id)

    if request.method == "POST":
        remark = request.POST.get("remark")
        report.doctor_remark = remark
        report.save()

        return redirect('doctor_dashboard')  # redirect after save

    return render(request, "add_remark.html", {"report": report})
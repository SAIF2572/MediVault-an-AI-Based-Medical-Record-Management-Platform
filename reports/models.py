from django.db import models
from patients.models import Patient
from django.utils import timezone


class Report(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    report_type = models.CharField(max_length=100, default="General")

    report_file = models.FileField(upload_to="reports/")

    uploaded_at = models.DateTimeField(default=timezone.now)

    doctor_remark = models.TextField(blank=True, null=True)

    ai_category = models.CharField(max_length=100, blank=True, null=True)

    ai_summary = models.TextField(blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.uhid} - {self.report_type}"
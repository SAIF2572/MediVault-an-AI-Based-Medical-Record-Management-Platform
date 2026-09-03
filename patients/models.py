import uuid
from django.db import models
from hospitals.models import Doctor
from django.utils import timezone

def generate_uhid():
    return "UHID-" + str(uuid.uuid4().hex[:8]).upper()


class Patient(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,default='Male')
    #mobile = models.CharField(max_length=15)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    

    doctor = models.ForeignKey('hospitals.Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    appointment_datetime = models.DateTimeField(default=timezone.now)

    uhid = models.CharField(
        max_length=20,
        unique=True,
        default=generate_uhid,
        editable=False
    )

    def __str__(self):
        return f"{self.name} - {self.uhid}"
from django.contrib import admin
from .models import Hospital, Department, Doctor

admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Doctor)
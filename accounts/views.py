from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from hospitals.models import Doctor
from patients.models import Patient

User = get_user_model()


#  DOCTOR LOGIN
def doctor_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        # Role check
        if user is not None and user.role == "doctor":
            login(request, user)
            return redirect("/doctor/search/")

        else:
            return render(request, "doctor_login.html", {
                "error": "Invalid doctor credentials"
            })

    return render(request, "doctor_login.html")


# PATIENT LOGIN 
def patient_login(request):

    if request.method == "POST":

        identifier = request.POST.get("identifier")
        password = request.POST.get("password")

        user = None

        #  Try Email
        try:
            user = User.objects.get(email=identifier)
        except:
            pass

        #  Try Phone
        if not user:
            try:
                user = User.objects.get(phone=identifier)
            except:
                pass

        # Try UHID (Patient table)
        if not user:
            try:
                patient = Patient.objects.get(uhid=identifier)
                user = User.objects.filter(email=patient.email).first()
            except:
                pass

        # Final check
        if user and user.check_password(password) and user.role == "patient":
            login(request, user)
            return redirect("/patient/dashboard/")

        return render(request, "patient_login.html", {
            "error": "Invalid credentials"
        })

    return render(request, "patient_login.html")


#  PATIENT REGISTER + UHID + EMAIL
User = get_user_model()

def register(request):

    doctor_id = request.GET.get("doctor")
    doctor = Doctor.objects.filter(id=doctor_id).first()

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        appointment_datetime = request.POST.get("appointment_datetime")

        # check existing user
        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "User already exists",
                "doctor": doctor
            })

        # Patient create
        patient = Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            address=address,
            phone=phone,
            email=email,
            doctor=doctor,
            appointment_datetime=appointment_datetime 
        )

        # User create
        user = User.objects.create(
            username=name,
            email=email,
            role="patient"
        )

        if hasattr(user, "phone"):
            user.phone = phone

        user.password = make_password(password)
        user.save()

        # EMAIL
        send_mail(
            subject="MediVault Registration Successful",
            message=f"""
Hello {name},

Your registration is successful.

-----------------------------
Patient Name: {name}
Doctor Name: {doctor.name if doctor else "Not Assigned"}
UHID Number: {patient.uhid}

Login Details:
Email / Phone / UHID: {email} OR {phone} OR {patient.uhid}
Password: {password}
-----------------------------
""",
            from_email="your_email@gmail.com",
            recipient_list=[email],
            fail_silently=True,
        )

        return redirect(f"/patient/success/?patient_id={patient.id}")

    return render(request, "register.html", {"doctor": doctor})
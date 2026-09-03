from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.lab_upload, name="lab_upload"),
    path("view/<int:report_id>/", views.view_report, name="view_report"),
    path('remark/<int:report_id>/', views.add_remark, name='add_remark'),
]
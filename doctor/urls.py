from django.urls import path
from .views import *
from doctor.views import approved_doctors_list, DoctorDetailView
from doctor.views import book_appointment,DoctorUserList
urlpatterns = [
    path('doctor/', approved_doctors_list, name='doctors'),
    path('doctor/detail/<int:pk>/', DoctorDetailView.as_view(), name="doctorview"),
    path('book_appointment/<int:pk>/', book_appointment, name='book_appointment'),
    path('appointment-success/', appointment_success, name='appointment_success'),
    path("approvel/<int:id>/",request_approval,name="approve"),
    path("doctor/doctorpanel/", DoctorUserList.as_view(), name="doctorpanel"),
    path('doctor_profile/', doctor_profile, name="doctor_profile"),
    path('update/<int:pk>', DoctorProfileUpdateView.as_view() , name="changeprofile"),

]

     
     
     
     

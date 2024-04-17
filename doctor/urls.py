from django.urls import path
from doctor.views import appointment_success
from doctor.views import approved_doctors_list, DoctorDetailView
from doctor.views import book_appointment,DoctorUserList
urlpatterns = [
    path('doctor/', approved_doctors_list, name='doctors'),
    path('doctor/detail/<int:pk>/', DoctorDetailView.as_view(), name="doctorview"),
    path('book_appointment/<int:pk>/', book_appointment, name='book_appointment'),
    path('appointment-success/', appointment_success, name='appointment_success'),

    path("doctor/doctorpanel/", DoctorUserList.as_view(), name="doctorpanel"),

]

     
     
     
     

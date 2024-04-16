from django.urls import path
from .views import *
from doctor.views import *

urlpatterns = [


    path('doctor/',approved_doctors_list , name='doctors'),
    path('doctor/detail/<int:pk>/',DoctorDetailView.as_view(),name="doctorview"),
    path('book_appointment/<int:doctor_id>/', book_appointment, name='book_appointment'),
]


     
     
     
     

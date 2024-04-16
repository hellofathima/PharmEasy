from django.shortcuts import render,redirect
from doctor.models import *
from doctor.forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404



# Create your views here.
# views.py

from autherization.models import Doctor

def approved_doctors_list(request):
    # Filter doctors who are approved by the admin
    approved_doctors = Doctor.objects.filter(is_active=True)

    
    return render(request, 'medicines/doctors.html', {'approved_doctors':approved_doctors})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from doctor.models import Booking
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

# def book_appointment(request, user_id):
#     doctor = Doctor.objects.get(user_id=user_id)  # Retrieve the doctor instance based on the user_id
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             # If the form is valid, save the form data along with the doctor instance
#             form.instance.doctor = doctor
#             form.save()
#             # Redirect to a success page
#             return redirect('appointment_success')
#     else:
#         # Pass the doctor instance to the form as initial data
#         form = BookingForm(initial={'doctor': doctor})
#     return render(request, 'medicines/appointment.html', {'form': form})

# def appointment_success(request):
#     return render(request, 'medicines/appointmentsuccess.html')




from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Doctor

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Doctor

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Doctor

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Doctor

from django.shortcuts import get_object_or_404

def book_appointment(request, doctor_id):
    # Get the doctor instance
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get the current user and assign it to the patient field
            patient = request.user
            form.instance.patient = patient
            form.instance.doctor = doctor
            form.save()
            return redirect('appointment_success')
    else:
        form = BookingForm(doctor=doctor)
    return render(request, 'medicines/appointment.html', {'form': form})



from django.views.generic import DetailView
from .models import Doctor

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor/doctorprofile_for_user.html'  
    context_object_name = 'doctor'




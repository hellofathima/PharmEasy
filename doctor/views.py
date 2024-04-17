from django.shortcuts import render,redirect
from doctor.models import *
from doctor.forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView,View
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.views.generic import TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.decorators.cache import never_cache
# Create your views here.
# views.py

from autherization.models import Doctor

def approved_doctors_list(request):
    # Filter doctors who are approved by the admin
    approved_doctors = Doctor.objects.filter(is_active=True)

    
    return render(request, 'medicines/doctors.html', {'approved_doctors':approved_doctors})


from django.shortcuts import render, redirect, get_object_or_404

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

















from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm

from django.shortcuts import render, redirect, get_object_or_404
from doctor.models import Doctor
from .forms import BookingForm

def book_appointment(request, pk):
    # Get the doctor instance
    doctor = get_object_or_404(Doctor, id=pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get the current user and assign it to the patient field
            patient = request.user
            form.instance.patient = patient
            form.instance.doctor = doctor  # Assign the Doctor instance directly
            
            # Fetch the department information from the related Doctor instance
            department = None
            if hasattr(doctor, 'department'):
                department = doctor.department.name  # Assuming 'name' is the attribute representing the department's name
            
            form.instance.department = department
            doctor.has_requested = True
            form.save()
            return redirect('appointment_success')
    else:
        # Initialize the form with doctor prepopulated
        form = BookingForm(initial={'doctor': doctor.id})  # Populate doctor field with doctor's id
        if hasattr(doctor, 'department'):
            form.fields['department'].initial = doctor.department.name
        
    return render(request, 'medicines/appointment.html', {'form': form})



from django.views.generic import DetailView
from .models import Doctor

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor/doctorprofile_for_user.html'  
    context_object_name = 'doctor'


def appointment_success(request):
    return render(request, 'medicines/appointmentsuccess.html')

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class DoctorUserList(ListView):
    model = Booking
    template_name = 'medicines/doctor_panel.html'
    context_object_name = "doctor_user"

    def get_queryset(self):
    #    nurse=self.request.user
       queryset = super().get_queryset()

       queryset = queryset.filter(doctor=self.request.user.id,is_confirmed=False)
       return queryset
    





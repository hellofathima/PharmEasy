from django import forms
from autherization.models import *
from doctor.models import *

from django import forms
from .models import Doctor, Booking
from autherization.models import *
from doctor.models import *
# class BookingForm(forms.ModelForm):
#     doctor = forms.ModelChoiceField(queryset=Doctor.objects.all().order_by('name'))
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     Department = forms.ChoiceField(choices=[])

#     class Meta:
#         model = Booking
#         fields = ['doctor', 'date', 'time', 'reason', 'Department']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['Department'].choices = self.get_department_choices()

#     def get_department_choices(self):
#         return [(Department, Department) for Department in Doctor.objects.values_list('Department', flat=True).distinct()]


#     def get_doctor_choices(self):
#         doctors = Doctor.objects.all()
#         return [(doctor.id, doctor.name) for doctor in doctors]


# class BookingForm(forms.ModelForm):
#     # Define the doctor field as a ModelChoiceField
#     doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=True)
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

#     class Meta:
#         model = Booking
#         fields = ['doctor', 'date', 'time', 'reason', 'department']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Make the doctor field read-only
#         self.fields['doctor'].widget.attrs['readonly'] = True
#         self.fields['doctor'].widget.attrs['disabled'] = True


from django import forms
from .models import Booking

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'style': 'width: 200px; height: 40px; padding: 5px;'}),
        }

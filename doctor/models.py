
from django.db import models
from autherization.models import *
from django.db import models
from autherization.models import *

class Booking(models.Model):
    # Your existing fields
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    
    # Add choices to the department field
    DEPARTMENT_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Orthopedics', 'Orthopedics'),
        ('Neurology', 'Neurology'),
        ('Oncology', 'Oncology'),
        ('Pediatrics', 'Pediatrics'),
        ('Gynecology', 'Gynecology'),
        ('Dermatology', 'Dermatology'),
        ('Psycology', 'Psycology'),
    ]
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES,default='Cardiology',null=True)

    def __str__(self):
        return f"Booking for {self.patient.username} with {self.doctor.user.username} on {self.date} at {self.time}"
    


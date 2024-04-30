from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.



class NormalUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    profile = models.TextField( null=True, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    Department = models.CharField(max_length=20, null=True)  # Add department field
    Designation = models.CharField(max_length=20, null=True)


class Customer(models.Model):
    user = models.OneToOneField(NormalUser, on_delete=models.CASCADE) 
    phone = models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    license_number = models.CharField(max_length=20, unique=True)
    Designation = models.CharField(max_length=20, null=True)
    Department = models.CharField(max_length=20, null=True)  # Add department field
    phone = models.IntegerField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    profile = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True)
    is_available = models.BooleanField(default=True, null=True)
    has_requested= models.BooleanField(default=False)

    # def __str__(self):
    #     return self.user.username 
    def __str__(self):
        return self.name if self.name else f"Doctor {self.pk}"
# 
class Feedback(models.Model):
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Feedback from {self.user.username} at {self.created_at}"
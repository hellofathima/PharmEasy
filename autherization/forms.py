from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomerSignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = NormalUser
        fields = ('username', 'email', 'phone', 'password1', 'password2','address')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Example@gmail.com'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),

        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            customer = Customer.objects.create(user=user, phone=self.cleaned_data['phone'])
            customer.save()
        return user
    

class DoctorSignUpForm(UserCreationForm):
    license_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = NormalUser
        fields = ('username', 'email', 'name', 'license_number', 'password1', 'password2', 'image', 'profile', 'address', 'phone','Department','Designation')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Example@gmail.com'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'profile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your work experience'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'designation':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Desigantion'}),
            'department':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Departmrnt'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            doctor = Doctor.objects.create(user=user,name=self.cleaned_data['name'], license_number=self.cleaned_data['license_number'], phone=self.cleaned_data['phone'], image=self.cleaned_data['image'], profile=self.cleaned_data['profile'], address=self.cleaned_data['address'],Designation=self.cleaned_data['Designation'],Department=self.cleaned_data['Department'])
            doctor.save()
        return user
   






class AdminForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=100)    



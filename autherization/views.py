from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from django.contrib.auth import logout
from django.core.validators import RegexValidator
from medicines.models import *
from devices.models import *
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from doctor.models import *
from datetime import datetime


def index(request):
    feedbacks = Feedback.objects.all()[:4]
    current_date = datetime.now().date()
    medicines = Medicine_inventory.objects.filter(expiry_date__gte=current_date)[:6]
    devices = DeviceInformation.objects.all()[:4]
    return render(request, "autherization/index.html", {'feedbacks': feedbacks, 'medicines': medicines, 'devices':devices})


def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            em = request.POST.get('email')
            form.save()
            subject = "Welcome to PharmEasy!"
            message = (
                f"Dear Customer,\n\n"
                "Thank you for creating an account with PharmEasy! "
                "We're thrilled to have you on board.\n\n"
                "Feel free to explore our website and discover a world of exciting products and services tailored just for you.\n\n"
                "If you have any questions or need assistance, don't hesitate to reach out to us.\n\n"
                "Best regards,\n"
                "The PharmEasy Team"
            )
            email_from = "pharmeasy305@gmail.com"
            email_to = em
            send_mail(subject, message, email_from, [email_to])
            return redirect('login')
    else:
        form = CustomerSignUpForm()
    return render(request, 'autherization/customersignup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            em = request.POST.get('email')
            form.save()
            subject = "Welcome to PharmEasy!"
            message = (
                f"Dear Customer,\n\n"
                "Thank you for creating an account with PharmEasy! "
                "We're thrilled to have you on board.\n\n"
                "Feel free to explore our website and discover a world of exciting products and services tailored just for you.\n\n"
                "If you have any questions or need assistance, don't hesitate to reach out to us.\n\n"
                "Best regards,\n"
                "The PharmEasy Team"
            )
            email_from = "pharmeasy305@gmail.com"
            email_to = em
            send_mail(subject, message, email_from, [email_to])
            return redirect('login')
    else:
        form = DoctorSignUpForm()
    return render(request, 'autherization/Doctorsignup.html', {'form': form})

def base(request):
    return render(request, "base.html")

def base3(request):
    return render(request, "base3.html")




# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
            
#             if user.is_doctor:  
#                 return redirect('doctorpanel')  
#             elif user.is_customer:
#                 return redirect('customerpanel') 
            
#             else:
                
#                 return redirect('index')
            
#         # return redirect('index')
#         else:
            
#             messages.error(request, 'Invalid username or password. Please try again.')
#             return redirect('login')  
#     else:

#         form = AuthenticationForm()
#     return render(request, 'autherization/login.html', {'form': form})









from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect, render

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.is_doctor:
                return redirect('doctorpanel')  
            elif user.is_customer:
                return redirect('customerpanel') 
            else:
                return redirect('index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('autherization:login_view')  
    else:
        form = AuthenticationForm()
    return render(request, 'autherization/login.html', {'form': form})


@login_required(login_url='/login/')
@never_cache
def customer_panel_view(request):
    feedbacks = Feedback.objects.all()[:4]
    current_date = datetime.now().date()
    medicines = Medicine_inventory.objects.filter(expiry_date__gte=current_date)[:6]
    devices = DeviceInformation.objects.all()[:4]

    return render(request, "autherization/customer_panel.html", {'feedbacks': feedbacks, 'medicines': medicines, 'devices':devices})


def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            user = request.user
            feedback = Feedback.objects.create(user=user, comment=comment)
            feedback.save()
            return redirect('feedback_success') 
            # return HttpResponse("success")
    else:
        form = FeedbackForm()

    return render(request, 'autherization/add_feedback.html',{'form':form})


class FeedBackSuccess(TemplateView):
    template_name = "autherization/feedback_success.html"


def doctor_panel_view(request):
    doctor = request.user.doctor
    bookings = Booking.objects.filter(is_confirmed = True , doctor = doctor).order_by("time"and"date")
    return render(request, 'autherization/doctor_panel.html', {'bookings': bookings})



def admin_login(request):
    if request.method == "POST":
        a = AdminForm(request.POST)
        if a.is_valid():
            unm = a.cleaned_data['username']
            ps = a.cleaned_data['password']
            user = authenticate(request, username=unm, password=ps)
            if user is not None:

                return redirect("adminpanel")
            else: 
                return HttpResponse("login failed!")
    return render(request, "autherization/adminlogin.html")

def admin_panel_view(request):
    return render(request, "autherization/adminpanel.html")


def forgot_password(request):
    user_list = NormalUser.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        
       
        for user in user_list:
            if user.email == email and user.username == username:
                user_id = user.id
                otp = get_random_string(length=6, allowed_chars='1234567890')
                print(f"Generated OTP: {otp}")
                request.session['otp'] = otp
                subject = "Password reset"
                message = f"Hi {username},\n\nSomeone has requested a new password for the following account on PharmEasy.\nIf you didn't make this request, please ignore this email.\nTo reset your password, please use the following OTP (One-Time Password): {otp} .\n\nThanks for using PharmEasy."
                email_from = "pharmeasy305@gmail.com"
                email_to = email
                send_mail(subject, message, email_from, [email_to])
                return redirect('change_password', user_id)
        else:
            return HttpResponse("Oops somthing went wrong !")
    return render(request, "autherization/forgot_password.html")



def change_password(request, id):
    user = NormalUser.objects.get(id=id)
    if request.method == "POST":
        otp = request.POST.get('otp')
        print(f"Submitted OTP: {otp}")
        if otp == request.session['otp']:
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                user.set_password(password1)
                user.save()
                return redirect("login")
            else:
                msg = 'Sorry something went wrong!'
                return render(request, 'autherization/success.html', {'msg': msg})
        else:
            msg = "otp doesn't match!"
            return render(request, 'autherization/success.html', {'msg': msg})   
    return render(request, "autherization/change_password.html")

def logout_view(request):
    logout(request)
    return redirect(login_view)

def aboutus(request):
    return render(request, "autherization/about.html")

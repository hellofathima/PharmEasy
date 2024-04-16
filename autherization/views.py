from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "autherization/index.html")

from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.core.validators import RegexValidator


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
            
        # return redirect('index')
        else:
            
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')  
    else:

        form = AuthenticationForm()
    return render(request, 'autherization/login.html', {'form': form})


def customer_panel_view(request):
    return render(request, 'autherization/customer_panel.html')


def   doctor_panel_view(request):
    return render(request, 'autherization/doctor_panel.html')



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
                subject = "Password reset"
                message = f"Hi {username},\n\nSomeone has requested a new password for the following account on PharmEasy.\nIf you didn't make this request, please ignore this email.\nTo reset your password, Click the following link: http://127.0.0.1:8000/autherization/change_password/{user_id}.\n\nThanks for using PharmEasy."
                email_from = "pharmeasy305@gmail.com"
                email_to = email
                send_mail(subject, message, email_from, [email_to])
                return redirect(reset_password)
        else:
            return HttpResponse("Oops somthing went wrong !")
    return render(request, "autherization/forgot_password.html")



def reset_password(request):
    return render(request, "autherization/reset_password.html")


def change_password(request, id):
    a = NormalUser.objects.get(id=id)
    if request.method == "POST":
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            a.set_password(p1)
            a.save()
            return HttpResponse("Password changed")
        else:
            return HttpResponse("Sorry something went wrong !")
    return render(request, "autherization/change_password.html")

def logout_view(request):
    logout(request)
    return redirect(login_view)

def aboutus(request):
    return render(request, "autherization/about.html")

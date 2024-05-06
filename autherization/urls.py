from django.contrib import admin
from django.urls import path,include
from autherization.views import *
urlpatterns = [

path('',index,name='index'),

path('signup/customer/', customer_signup, name='customer_signup'),
path('signup/doctor/', doctor_signup, name='Doctor_signup'),
path('login/', login_view, name='login'),

path('base/', base),
path('base3/', base3),
path('customerpanel/', customer_panel_view, name='customerpanel'),
path('doctorpanel/', doctor_panel_view, name='doctorpanel'),
path('adminrpanel/', admin_panel_view, name='adminpanel'),

path('aboutus/', aboutus, name='aboutus'),

path('admin_login/', admin_login, name="admin_login"),

path('forgot/', forgot_password, name="forgot_password"),
path('change_password/<int:id>', change_password, name="change_password"),

path('logout/', logout_view, name="logout_view"),
path('success/', add_feedback, name="add_feedback"),
path('feedback_success/', FeedBackSuccess.as_view(), name="feedback_success"),

]
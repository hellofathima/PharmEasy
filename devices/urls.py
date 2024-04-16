from django.urls import path
from devices.views import *

urlpatterns = [

path('devices/list/', dev_list,name="listdevices"),

# urls.py
path('devices/detail/<int:pk>/', DeviceDetailView.as_view(), name='device_detail'),
   
]# urls.py




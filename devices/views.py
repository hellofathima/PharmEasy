from django.shortcuts import render
from devices.models import *
# Create your views here.
from django.shortcuts import render
from devices.models import DeviceInformation
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
def dev_list(request):
    devices = DeviceInformation.objects.all()
    return render(request, 'clinicaldevices/listdevices.html', {'devices': devices})



# def DeviceDetails(request, id):
#     device = get_object_or_404(DeviceInformation, id=id)
#     return render(request, "clinicaldevices/devicedetail.html", {"device": device})

# views.py

from django.views.generic import DetailView

class DeviceDetailView(DetailView):
    model = DeviceInformation
    template_name = 'clinicaldevices/devicedetail.html'
    context_object_name = 'device'

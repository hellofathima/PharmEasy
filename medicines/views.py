from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from .models import Medicine_inventory
from medicines.models import *
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView,View

# Create your views here.
# views.py

from django.shortcuts import render
from .models import Medicine_inventory
from devices.models import * 
from django.db.models import Q

def medicines_list(request):
    medicines = Medicine_inventory.objects.all()
    return render(request, 'medicines/listmed.html', {'medicines': medicines})

# def search_medicines(request):
#     query = request.GET.get('q')
#     if query:
#         medicines = Medicine_inventory.objects.filter(Q(medicine_name__icontains=query) | Q(manufacturer__icontains=query))
#         devices = DeviceInformation.objects.filter(product_name__icontains=query)
#         medicines = list(medicines) + list(devices)
#     else:
#         medicines = []
#     return render(request, 'medicines/searchmedicine.html', {'medicines': medicines, 'query':query,'devices':devices})

from django.db.models import Q
from medicines.models import Medicine_inventory
from django.shortcuts import render
from devices.models import *

def search_medicines(request):
    query = request.GET.get('q')
    medicines = []
    
    if query:
        # Search for medicines containing the query in medicine_name or manufacturer
        medicine_results = Medicine_inventory.objects.filter(
            Q(medicine_name__icontains=query) | Q(manufacturer__icontains=query)
        )
        
        # Search for devices containing the query in product_name
        device_results = DeviceInformation.objects.filter(product_name__icontains=query)
        
        # Combine medicine and device results into a single list
        medicines = list(medicine_results) + list(device_results)
    
    return render(request, 'medicines/searchmedicine.html', {'medicines': medicines, 'query': query})

                                                       

def medicine_details(request, pk):
    medicine = get_object_or_404(Medicine_inventory, pk=pk)
    return render(request, 'medicines/detail.html', {'medicine': medicine})



class HairfallView(TemplateView):
    template_name = 'medicines/hairfall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hairfall_category =Medicine_Category.objects.get(category_name='hairfall')
        context['medicines'] = Medicine_inventory.objects.filter(category= hairfall_category )
        return context
    
class HairfallDetailView(DetailView):
    template_name = "medicines/hairfalldetail.html"  
    model=Medicine_inventory
    context_object_name="medicine"   


class BabyCareMedicinesView(TemplateView):
    template_name = 'medicines/babycare.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baby_care_category = Medicine_Category.objects.get(category_name='BabyCare')
        context['medicines'] = Medicine_inventory.objects.filter(category=baby_care_category)
        return context
    

class BabyCareDetailView(DetailView):
    template_name="medicines/babycaredetail.html"
    model=Medicine_inventory
    context_object_name="medicine"    
    
class BeautyCareMedicinesView(TemplateView):
    template_name = 'medicines/beautycare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        beauty_and_care_category =   Medicine_Category.objects.get(category_name='beauty and care')
        context['medicines'] = Medicine_inventory.objects.filter(category=beauty_and_care_category)
        return context
    
class BeautyCareDetailView(DetailView):
    template_name = "medicines/beautydetail.html"  
    model=Medicine_inventory
    context_object_name="medicine"

    
class NutritionView(TemplateView):
    template_name = 'medicines/nutritionandsupplements.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nutrition_and_care_category =   Medicine_Category.objects.get(category_name='nutrition and supplements')    
        context['medicines'] = Medicine_inventory.objects.filter(category=nutrition_and_care_category )
        return context
    
class NutritionDetailView(DetailView):
    template_name = "medicines/nutritiondetail.html"  
    model=Medicine_inventory
    context_object_name="medicine"

    
class DiabetesView(TemplateView):
    template_name = 'medicines/diabetis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        diabetes_category =   Medicine_Category.objects.get(category_name='Diabetes')    
        context['medicines'] = Medicine_inventory.objects.filter(category=diabetes_category)
        return context
    
class DiabetesDetailView(DetailView):
    template_name = "medicines/diabetisdetails.html"  
    model=Medicine_inventory
    context_object_name="medicine"   





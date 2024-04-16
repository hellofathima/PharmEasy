from django.urls import path
from .views import *

urlpatterns = [
path('medicines/list', medicines_list, name='medicines_list'),

    # urls.py

path('search/', search_medicines, name='search-medicine'),


path('medicine/<int:pk>/', medicine_details, name='medicine_details'),
path('hairfall/',  HairfallView.as_view(), name='hairfall'),
path('hairfall_detail/<int:pk>/',HairfallDetailView.as_view(), name="hairfall_detail"),

path('babycare/', BabyCareMedicinesView.as_view(), name='babycare'),
path('babycare_detail/<int:pk>/',BabyCareDetailView.as_view(), name="babycare_detail"),

path('beautycare/', BeautyCareMedicinesView.as_view(), name='beautycare'),
path('beautycare_detail/<int:pk>/',BeautyCareDetailView.as_view(), name="beautycare_detail"),

path('nutrition/',  NutritionView.as_view(), name='nutrition'),
path('nutrition_detail/<int:pk>/',NutritionDetailView.as_view(), name="nutrition_detail"),

path('diabetes/',  DiabetesView.as_view(), name='diabetes'),
path('diabetes_detail/<int:pk>/',DiabetesDetailView.as_view(), name="diabetes_detail"),

]


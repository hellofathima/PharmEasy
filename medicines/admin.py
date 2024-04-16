from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Medicine_Category)
admin.site.register(Medicine_inventory)


# admin.py
# admin.py
from django.contrib import admin
from .models import ExpiredMedicine

class ExpiredMedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'expiry_date')

admin.site.register(ExpiredMedicine, ExpiredMedicineAdmin)


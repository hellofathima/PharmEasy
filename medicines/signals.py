# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Medicine_inventory, ExpiredMedicine

@receiver(post_save, sender=Medicine_inventory)
def check_expiry_and_add(sender, instance, **kwargs):
    if instance.expiry_date and instance.expiry_date < timezone.now():
        ExpiredMedicine.objects.create(medicine=instance, expiry_date=instance.expiry_date)

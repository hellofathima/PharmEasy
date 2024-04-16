from django.db import models

# Create your models here.
class DeviceInformation(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    product_image = models.ImageField(upload_to="images/", null=False,blank=False)
    phone = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.product_name
    
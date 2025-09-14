from django.db import models
from django.contrib.auth.models import User


class sabad(models.Model):   
    sabad = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=100, default="0") 

    def __str__(self):
        return f"سبد {self.sabad.username}"


class iteam(models.Model):   
    cart = models.ForeignKey(sabad, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="item") 
    price = models.CharField(max_length=50, default="0")     

    def __str__(self):
        return self.name


class Iteam_sabad(models.Model):   
    cart = models.ForeignKey(sabad, on_delete=models.CASCADE, related_name="iteam_token")
    ite = models.ForeignKey(iteam, on_delete=models.CASCADE)  
    qty = models.IntegerField(default=1) 

    def __str__(self):
        return f"{self.qty} × {self.ite.name} در {self.cart.sabad.username}"

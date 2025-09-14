from django.db import models

# Create your models here.

class My_model(models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField()
    price = models.CharField(max_length=100_000_000)
    img = models.ImageField(upload_to='img/', null=True , blank=True)
    code = models.CharField(max_length=4)
    data = models.DateTimeField(auto_now_add=True)
    

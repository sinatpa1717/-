from django.db import models

# Create your models here.

class comment_model(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    phone = models.CharField(max_length=11)

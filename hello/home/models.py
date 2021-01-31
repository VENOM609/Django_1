from django.db import models

# Create your models here.
class contact(models.Model):
    phone =models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    reasion=models.TextField()
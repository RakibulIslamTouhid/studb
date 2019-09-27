from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=7)
    dept = models.CharField(max_length=200)
    sec = models.CharField(max_length=2)
    blood = models.CharField(max_length=5)
    image = models.ImageField(upload_to='images/')
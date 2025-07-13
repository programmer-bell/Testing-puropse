from django.db import models
from django.utils import timezone

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    catagory = models.CharField(max_length=20,
    choices=(('A-Class','AC'),('B-Class','BC'),('C-Class','CC'),('D-Class','DC')))
    bio = models.TextField(max_length=100)
    number = models.IntegerField()
    is_active = models.BooleanField(null=True,blank=True)
    is_open = models.DateTimeField(default=timezone.now)

                                    

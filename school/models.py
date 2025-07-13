from django.db import models
from django.utils import timezone
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    is_government = models.BooleanField(null=True,blank=True)
    is_scolarshpis = models.BooleanField(null=True,blank=True)
    bio = models.TextField(max_length=100)
    number = models.IntegerField()
    grade = models.CharField(max_length=100,choices=( ('A++','1'),('B++','2'),('C++','3') ))
    email = models.EmailField(max_length=100)
    is_open = models.DateTimeField(default=timezone.now)

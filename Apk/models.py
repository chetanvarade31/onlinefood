from ast import Try
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.forms import widgets

from django.utils import timezone
import time
# Create your models here.
curr_time = time.localtime()
class Category(models.Model):
    name = models.CharField(max_length=122, null= True)

    def __str__(self):
        return str(self.name)
class Hotels(models.Model):
    
    name = models.CharField(max_length=122,null= True)
    table = models.PositiveIntegerField()
    photo = models.ImageField(upload_to = 'media')
    zipcode = models.CharField(max_length=8,default=000000)

    def __str__(self):
        return str(self.name)
        

class Product(models.Model):
    name = models.CharField(max_length=122)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category,on_delete= models.CASCADE,default= None)
    description = models.TextField()
    hotel_name = models.ForeignKey(Hotels,on_delete=models.CASCADE,default= None ,null= True)
    product_image = models.ImageField(upload_to = 'media')

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12,unique= True)
    address = models.CharField(max_length= 155)
    city = models.CharField(max_length= 155, default= 1)
    district = models.CharField(max_length= 155, default= 1)
    state = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    zipcode = models.CharField(max_length=8)

    def __str__(self):
        return str(self.user)


CHOICES = (
    ('Pending','Pending'),
    ('Rejected','Rejected'),
    ('Approved','Approved'),
    ('Picked By Courier','Picked By Courier'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered')
)

class Table(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    name = models.CharField(max_length=122)
    persons = models.IntegerField()
    tables = models.IntegerField()
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    mobile = models.CharField(max_length=122)
    hotel_name = models.CharField(max_length=122)


class Order(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE )
    name = models.CharField(max_length=122)
    category = models.CharField(max_length=122)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(default= timezone.now)
    status = models.CharField(choices= CHOICES,max_length= 155,default= 'Pending', null= True)
    product_img = models.ImageField()
    

class Reviews(models.Model):
    hotel_name = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    message = models.TextField(max_length=255)
    date = models.DateField(default= timezone.now)
    time = models.TimeField(default= time.strftime("%H:%M:%S", curr_time))
from django import forms

from django.core.exceptions import ValidationError
from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from .models import Buydb
    



# 創建一個 Raw Form
class BuydbForm(forms.Form):
    Title = forms.CharField(help_text="Enter buydb title")
    MrtName = forms.CharField(help_text="Enter Mrt Station Code, ex: R12 = 雙連捷運站")
    MrtName = forms.CharField(help_text="Enter Mrt Station Name, ex: R12 = 雙連捷運站")
    Address = forms.CharField(help_text="Enter Address")
    FloorType = forms.CharField(help_text="Enter 整層住家 or 套房")
    RoomNum = forms.IntegerField(help_text="Enter Room Number, ex: 4 = 4房")
    Price = forms.IntegerField(help_text="Enter buying prices per month, 單位 = 新台幣")
    Size = forms.DecimalField(max_digits=20,decimal_places=2, help_text="Enter housing size, 單位 = 坪")
    Floor = forms.CharField(max_length=200, help_text="Enter floor")
    Parking = forms.CharField(max_length=200, help_text="Enter parking detail")
    Link = forms.CharField(max_length=500, help_text="Enter 591 urls")


    
# Model - Buydb
class Buydb2(models.Model):
    Title = models.CharField(max_length=200, help_text="Enter buydb title")
    MrtCode = models.CharField(max_length=200, help_text="Enter Mrt Station Code, ex: R12 = 雙連捷運站")
    MrtName = models.CharField(max_length=200, help_text="Enter Mrt Station Name, ex: R12 = 雙連捷運站")
    Address = models.CharField(max_length=200, help_text="Enter Address")
    FloorType = models.CharField(max_length=200, help_text="Enter 整層住家 or 套房")

    RoomNum = models.IntegerField(help_text="Enter Room Number, ex: 4 = 4房")
    Price = models.IntegerField(help_text="Enter buying prices per month, 單位 = 新台幣")
    Size = models.DecimalField(max_digits=20,decimal_places=2, help_text="Enter housing size, 單位 = 坪")
    Floor = models.CharField(max_length=200, help_text="Enter floor")
    Parking = models.CharField(max_length=200, help_text="Enter parking detail")
    Link = models.CharField(max_length=500, help_text="Enter 591 urls")

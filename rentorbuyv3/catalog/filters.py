from django import forms
from django.forms.formsets import MAX_NUM_FORM_COUNT
from .models import Buydb, Rentdb
import django_filters
 
#引用所要查詢的資料模型及django-filters
#接著，自訂過濾器類別(MovieFilter)，並且繼承自FilterSet類別
#再利用model及fields屬性來分別指定所要查詢的資料模型和欄位。
class BuydbFilter(django_filters.FilterSet):
    
    Price = django_filters.NumberFilter(
        lookup_expr='icontains',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Buydb
        fields = '__all__'





class RentdbFilter(django_filters.FilterSet):
    
    Price = django_filters.NumberFilter(
        lookup_expr='icontains',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        ordering = ["price"]
        model = Rentdb
        fields = '__all__'
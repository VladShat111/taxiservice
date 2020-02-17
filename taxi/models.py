from django.db import models
from django.utils import timezone
from django.forms import forms
# Create your models here.


class TaxiOrder(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=13, blank=False, null=False)
    start_address = models.CharField(max_length=200, blank=False, null=False)
    end_address = models.CharField(max_length=200, blank=False, null=True)
    desire_time = models.TimeField(blank=False, null=False)

    def __str__(self):
        return self.name


class Car(models.Model):
    order = models.ForeignKey(TaxiOrder, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=False)
    car_brand = models.CharField(max_length=100)

    def __str__(self):
        return self.car_brand

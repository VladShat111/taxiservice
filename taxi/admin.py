from django.contrib import admin
from .models import TaxiOrder, Car

# Register your models here.


@admin.register(TaxiOrder)
class TaxiOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'start_address', 'end_address', 'desire_time')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('order', 'active', 'car_brand')
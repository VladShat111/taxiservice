from django.forms import ModelForm
from .models import TaxiOrder

class TaxiOrderForm(ModelForm):
    class Meta:
        model = TaxiOrder
        fields = ['name', 'phone', 'start_address', 'end_address', 'desire_time']
        labels = {
            "name": "Ім'я",
            'phone': 'Номер телфону',
            'start_address': 'Поточна адреса',
            'end_address': 'Кінцева адреса',
            'desire_time': 'Час виклику авто'
        }

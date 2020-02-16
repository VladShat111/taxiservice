from django.forms import ModelForm, TextInput, forms
from .models import TaxiOrder
import re


class TaxiOrderForm(ModelForm):

    class Meta:
        model = TaxiOrder
        fields = '__all__'
        labels = {
            "name": "Ім'я",
            'phone': 'Номер телфону',
            'start_address': 'Поточна адреса',
            'end_address': 'Кінцева адреса',
            'desire_time': 'Час виклику авто'
        }
        widgets = {
            'phone': TextInput(attrs={'placeholder': '+380#########'}),
        }

    def clean_name(self):
        user_name = self.cleaned_data.get('name')
        text = re.findall('[А-ЯҐЄІЇ-ягєії]', user_name)
        en = re.findall('[A-Z-a-z]', user_name)
        if len(text) > 0 and len(en) == 0:
            return user_name
        else:
            raise forms.ValidationError('Тільки кирилиця')

    def clean_phone(self):
        phone_number = self.cleaned_data.get('phone')
        text = re.findall(r'^((\+380)+([0-9]){9})$', phone_number)
        if len(text) == 0:
            raise forms.ValidationError('Номер має відповідати такому вигляду - +380#########')
        return phone_number



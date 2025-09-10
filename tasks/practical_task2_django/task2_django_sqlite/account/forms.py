from django import forms
from django.core.exceptions import ValidationError
from .models import Staff


class StaffForm(forms.ModelForm):
    labor_contract = forms.IntegerField(max_value=9999)

    class Meta:
        model = Staff
        fields = [
            'full_name',
            'age',
            'salary',
            'labor_contract',
        ]

    def clean(self):
        cleaned_data = super().clean()
        labor_contract = cleaned_data.get('labor_contract')
        salary = cleaned_data.get('salary')

        if salary > 1000000:
            raise ValidationError({
                'salary': 'В нашей компании нету столько средств на содержание одного сотрудника'
            })
        return cleaned_data

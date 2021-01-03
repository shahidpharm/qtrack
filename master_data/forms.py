from django import forms
from .models import *


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_name']

        widgets = {
            'country_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['country', 'city_name']

        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'city_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class MeasuringUnitForm(forms.ModelForm):
    class Meta:
        model = MeasuringUnits
        fields = ['measuring_unit_name', 'measuring_unit_code']

        widgets = {
            'measuring_unit_name': forms.TextInput(attrs={'class': 'form-control'}),
            'measuring_unit_code': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_code', 'country']

        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('country', 'company', 'plant_name', 'plant_code')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['company'].queryset = Company.objects.none()

            if 'country' in self.data:
                try:
                    country_id = int(self.data.get('country'))
                    self.fields['company'].queryset = Company.objects.filter(country_id=country_id).order_by(
                        'company_name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty company queryset
            elif self.instance.pk:
                self.fields['company'].queryset = self.instance.country.company_set.order_by('company_name')

        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'plant_name': forms.TextInput(attrs={'class': 'form-control'}),
            'plant_code': forms.TextInput(attrs={'class': 'form-control'}),
        }


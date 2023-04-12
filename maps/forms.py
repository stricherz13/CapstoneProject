from django import forms
from django.forms import ModelForm
from .models import StLouisCityLandTax


class StLouisCityLandTaxForm(ModelForm):
    sale = forms.ModelMultipleChoiceField(label='Sale', widget=forms.Select, queryset=StLouisCityLandTax.objects.values_list('sale', flat=True).distinct().order_by('sale'), required=False)
    neighborho = forms.ModelMultipleChoiceField(label='Neighborhood', widget=forms.SelectMultiple, queryset=StLouisCityLandTax.objects.values_list('neighborho', flat=True).distinct().order_by('neighborho'), required=False)

    class Meta:
        model = StLouisCityLandTax
        fields = ['sale', 'neighborho']

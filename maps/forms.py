from django import forms
from django.forms import ModelForm, Form
from .models import StLouisCityLandTax


class StLouisCityLandTaxForm(Form):
    sale = forms.MultipleChoiceField(label='Sale', required=False)
    neighborho = forms.MultipleChoiceField(label='Neighborhood', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sale'].choices = StLouisCityLandTax.objects.values_list('sale', 'sale').distinct().order_by('sale')
        self.fields['neighborho'].choices = StLouisCityLandTax.objects.values_list('neighborho', 'neighborho').distinct().order_by('neighborho')

    #class Meta:
    #    model = StLouisCityLandTax
    #    fields = ['sale', 'neighborho']

from django import forms
from django.forms import Form
from .models import StLouisCityLandTax


class StLouisCityLandTaxForm(Form):
    sale = forms.MultipleChoiceField(label='Sale', required=True)
    neighborho = forms.MultipleChoiceField(label='Neighborhood', required=False)
    zip = forms.MultipleChoiceField(label='Zip code', required=False)
    landuse = forms.MultipleChoiceField(label="Land use", required=False)
    zoning = forms.MultipleChoiceField(label="Zoning", required=False)
    policedist = forms.MultipleChoiceField(label="Police district", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sale'].choices = StLouisCityLandTax.objects.values_list('sale', 'sale').distinct().order_by('sale')
        self.fields['neighborho'].choices = StLouisCityLandTax.objects.values_list('neighborho','neighborho').distinct().order_by('neighborho')
        self.fields['landuse'].choices = StLouisCityLandTax.objects.values_list('landuse', 'landuse').distinct().order_by('landuse')
        self.fields['zoning'].choices = StLouisCityLandTax.objects.values_list('zoning', 'zoning').distinct().order_by('zoning')
        self.fields['policedist'].choices = StLouisCityLandTax.objects.values_list('policedist', 'policedist').distinct().order_by('policedist')
        self.fields['zip'].choices = StLouisCityLandTax.objects.values_list('zip', 'zip').distinct().order_by('zip')



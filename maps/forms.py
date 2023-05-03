from django import forms
from django.forms import Form
from .models import StLouisCityLandTax, LRAModel, StLouisCityLandTaxModel2023


class StLouisCityLandTaxForm(Form):
    sale = forms.MultipleChoiceField(label='Sale', required=False)
    neighborho = forms.MultipleChoiceField(label='Neighborhood', required=False)
    zip = forms.MultipleChoiceField(label='Zip code', required=False)
    landuse = forms.MultipleChoiceField(label="Land use", required=False)
    zoning = forms.MultipleChoiceField(label="Zoning", required=False)
    policedist = forms.MultipleChoiceField(label="Police district", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sale'].choices = StLouisCityLandTax.objects.values_list('sale', 'sale').distinct().order_by('sale')
        self.fields['neighborho'].choices = StLouisCityLandTax.objects.values_list('neighborho',
                                                                                   'neighborho').distinct().order_by(
            'neighborho')
        self.fields['landuse'].choices = StLouisCityLandTax.objects.values_list('landuse',
                                                                                'landuse').distinct().order_by(
            'landuse')
        self.fields['zoning'].choices = StLouisCityLandTax.objects.values_list('zoning', 'zoning').distinct().order_by(
            'zoning')
        self.fields['policedist'].choices = StLouisCityLandTax.objects.values_list('policedist',
                                                                                   'policedist').distinct().order_by(
            'policedist')
        self.fields['zip'].choices = StLouisCityLandTax.objects.values_list('zip', 'zip').distinct().order_by('zip')


class LRAForm(Form):
    neighborho = forms.MultipleChoiceField(label='Neighborhood', required=False)
    ward20 = forms.MultipleChoiceField(label="Ward", required=False)
    vacantland = forms.MultipleChoiceField(label="Vacant lot", required=False)
    zip = forms.MultipleChoiceField(label='Zip code', required=False)
    landuse = forms.MultipleChoiceField(label="Land use", required=False)
    zoning = forms.MultipleChoiceField(label="Zoning", required=False)
    policedist = forms.MultipleChoiceField(label="Police district", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['neighborho'].choices = LRAModel.objects.values_list('neighborho',
                                                                         'neighborho').distinct().order_by('neighborho')
        self.fields['ward20'].choices = LRAModel.objects.values_list('ward20', 'ward20').distinct().order_by('ward20')
        self.fields['vacantland'].choices = LRAModel.objects.values_list('vacantland',
                                                                         'vacantland').distinct().order_by('vacantland')
        self.fields['landuse'].choices = LRAModel.objects.values_list('landuse', 'landuse').distinct().order_by(
            'landuse')
        self.fields['zoning'].choices = LRAModel.objects.values_list('zoning', 'zoning').distinct().order_by('zoning')
        self.fields['policedist'].choices = LRAModel.objects.values_list('policedist',
                                                                         'policedist').distinct().order_by('policedist')
        self.fields['zip'].choices = LRAModel.objects.values_list('zip', 'zip').distinct().order_by('zip')


class StLouisCityLandTaxForm2023(Form):
    sale = forms.MultipleChoiceField(label='Sale', required=False)
    neighborho = forms.MultipleChoiceField(label='Neighborhood', required=False)
    policedist = forms.MultipleChoiceField(label="Police district", required=False)
    zip = forms.MultipleChoiceField(label='Zip code', required=False)
    ward = forms.MultipleChoiceField(label="Ward", required=False)
    landuse = forms.MultipleChoiceField(label="Land use", required=False)
    zoning = forms.MultipleChoiceField(label="Zoning", required=False)
    numunits = forms.MultipleChoiceField(label="Units", required=False)
    vacantland = forms.MultipleChoiceField(label="Vacant lot", required=False)
    numbldgs = forms.MultipleChoiceField(label="Buildings", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sale'].choices = StLouisCityLandTaxModel2023.objects.values_list('sale',
                                                                                      'sale').distinct().order_by(
            'sale')
        self.fields['neighborho'].choices = StLouisCityLandTaxModel2023.objects.values_list('neighborho',
                                                                                            'neighborho').distinct().order_by(
            'neighborho')
        self.fields['policedist'].choices = StLouisCityLandTaxModel2023.objects.values_list('policedist',
                                                                                            'policedist').distinct().order_by(
            'policedist')
        self.fields['zip'].choices = StLouisCityLandTaxModel2023.objects.values_list('zip', 'zip').distinct().order_by(
            'zip')
        self.fields['ward'].choices = StLouisCityLandTaxModel2023.objects.values_list('ward20',
                                                                                      'ward20').distinct().order_by(
            'ward20')
        self.fields['landuse'].choices = StLouisCityLandTaxModel2023.objects.values_list('landuse',
                                                                                         'landuse').distinct().order_by(
            'landuse')
        self.fields['zoning'].choices = StLouisCityLandTaxModel2023.objects.values_list('zoning',
                                                                                        'zoning').distinct().order_by(
            'zoning')
        self.fields['numunits'].choices = StLouisCityLandTaxModel2023.objects.values_list('numunits',
                                                                                          'numunits').distinct().order_by(
            'numunits')
        self.fields['vacantland'].choices = StLouisCityLandTaxModel2023.objects.values_list('vacantland',
                                                                                            'vacantland').distinct().order_by(
            'vacantland')
        self.fields['numbldgs'].choices = StLouisCityLandTaxModel2023.objects.values_list('numbldgs',
                                                                                          'numbldgs').distinct().order_by(
            'numbldgs')

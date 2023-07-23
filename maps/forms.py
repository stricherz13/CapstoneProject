from django import forms
from django.forms import Form
from .models import StLouisCityLandTax, LRAModel, StLouisCityLandTaxModel2023, StCharles2023Model


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


class StCharlesCountyLandTaxForm(Form):
    municipali = forms.MultipleChoiceField(label='Municipality', required=False)
    proptype = forms.MultipleChoiceField(label='Property type', required=False)
    situszip = forms.MultipleChoiceField(label='Zip code', required=False)
    schooldist = forms.MultipleChoiceField(label="School district", required=False)
    bedrooms = forms.MultipleChoiceField(label="Bedrooms", required=False)
    bathrooms = forms.MultipleChoiceField(label="Bathrooms", required=False)
    halfbathro = forms.MultipleChoiceField(label="Half baths", required=False)
    garagestal = forms.MultipleChoiceField(label="Garage stalls", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['municipali'].choices = StCharles2023Model.objects.values_list('municipali',
                                                                                   'municipali').distinct().order_by(
            'municipali')
        self.fields['proptype'].choices = StCharles2023Model.objects.values_list('proptype',
                                                                                 'proptype').distinct().order_by(
            'proptype')
        self.fields['situszip'].choices = StCharles2023Model.objects.values_list('situszip',
                                                                                 'situszip').distinct().order_by(
            'situszip')
        self.fields['schooldist'].choices = StCharles2023Model.objects.values_list('schooldist',
                                                                                        'schooldist').distinct().order_by(
            'schooldist')
        self.fields['bedrooms'].choices = StCharles2023Model.objects.values_list('bedrooms',
                                                                                 'bedrooms').distinct().order_by(
            'bedrooms')
        self.fields['bathrooms'].choices = StCharles2023Model.objects.values_list('bathrooms',
                                                                                  'bathrooms').distinct().order_by(
            'bathrooms')
        self.fields['halfbathro'].choices = StCharles2023Model.objects.values_list('halfbathro',
                                                                                   'halfbathro').distinct().order_by(
            'halfbathro')
        self.fields['garagestal'].choices = StCharles2023Model.objects.values_list('garagestal',
                                                                                      'garagestal').distinct().order_by(
            'garagestal')

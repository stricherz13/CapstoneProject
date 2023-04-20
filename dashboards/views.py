from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class StLouisLandTaxDashboard2022(TemplateView):
    template_name = 'dashboards/2022StLouisLandTaxDashboard.html'

class LRADashboard2022(TemplateView):
    template_name = 'dashboards/2022LRADashboard.html'

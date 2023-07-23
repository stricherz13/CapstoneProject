from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class StLouisLandTaxDashboard2022(TemplateView):
    template_name = 'dashboards/2022StLouisLandTaxDashboard.html'

class StLouisLandTaxDashboard2023(TemplateView):
    template_name = 'dashboards/2023StLouisLandTaxDashboard.html'

class LRADashboard(TemplateView):
    template_name = 'dashboards/LRADashboard.html'

class StCharlesCountyLandTaxDashboard(TemplateView):
    template_name = 'dashboards/StCharlesCountyLandTaxDashboard.html'

from django.urls import path
from .views import StLouisLandTaxDashboard2022, LRADashboard2022

app_name = 'dashboards'

urlpatterns = [
    path("2022StLouisLandTaxDashboard", StLouisLandTaxDashboard2022.as_view(), name="2022StLouisLandTaxDashboard"),
    path("2022LRADashboard", LRADashboard2022.as_view(), name="2022LRADashboard")
]
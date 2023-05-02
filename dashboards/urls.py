from django.urls import path
from .views import StLouisLandTaxDashboard2022, LRADashboard, StLouisLandTaxDashboard2023

app_name = 'dashboards'

urlpatterns = [
    path("2022StLouisLandTaxDashboard", StLouisLandTaxDashboard2022.as_view(), name="2022StLouisLandTaxDashboard"),
    path("2023StLouisLandTaxDashboard", StLouisLandTaxDashboard2023.as_view(), name="2023StLouisLandTaxDashboard"),
    path("2022LRADashboard", LRADashboard.as_view(), name="2022LRADashboard")
]
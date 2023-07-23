from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path("2022StLouisLandTaxMap", views.combinedView, name='StLouisCityLandTaxSale'),
    path("2023StLouisLandTaxMap", views.combinedViewSTL2023, name='StLouisCityLandTaxSale2023'),
    path("LRAMap", views.LRAcombinedView, name='LRA'),
    path("2023StCharlesTaxMap", views.StCharles2023combinedView, name='StCharles2023')
]

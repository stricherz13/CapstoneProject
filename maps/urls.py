from django.urls import path
from . import views

app_name = 'maps'

urlpatterns = [
    path("2022StLouisLandTaxMap", views.combinedView, name='StLouisCityLandTaxSale'),
    path("LRAMap", views.LRAcombinedView, name='LRA')
]

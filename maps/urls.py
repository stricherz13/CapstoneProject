from django.urls import path
from . import views

urlpatterns = [
    path("StLouisCityLandTaxSale/", views.combinedView, name='combined_view'),

]

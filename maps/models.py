from django.db import models


class LRA2022(models.Model):
    handle = models.CharField(max_length=16, blank=True, null=True)
    siteaddr = models.CharField(max_length=254, blank=True, null=True)
    numunits = models.BigIntegerField(blank=True, null=True)
    vacantland = models.CharField(max_length=254, blank=True, null=True)
    numbldgs = models.BigIntegerField(blank=True, null=True)
    landarea = models.BigIntegerField(blank=True, null=True)
    frontage = models.FloatField(blank=True, null=True)
    bdg1year = models.BigIntegerField(blank=True, null=True)
    bdg1area = models.BigIntegerField(blank=True, null=True)
    bdg1strycd = models.BigIntegerField(blank=True, null=True)
    ward = models.BigIntegerField(blank=True, null=True)
    policedist = models.BigIntegerField(blank=True, null=True)
    zip = models.BigIntegerField(blank=True, null=True)
    zoning = models.CharField(max_length=254, blank=True, null=True)
    neighborho = models.CharField(max_length=254, blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True)
    point_x = models.FloatField(blank=True, null=True)
    point_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LRA_2022'


class StLouisCityLandTax(models.Model):
    land_id = models.CharField(max_length=254, blank=True, null=True)
    owner = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    handle = models.CharField(max_length=16, blank=True, null=True)
    numunits = models.BigIntegerField(blank=True, null=True)
    vacantland = models.CharField(max_length=254, blank=True, null=True)
    numbldgs = models.BigIntegerField(blank=True, null=True)
    landarea = models.BigIntegerField(blank=True, null=True)
    frontage = models.FloatField(blank=True, null=True)
    bdg1year = models.BigIntegerField(blank=True, null=True)
    bdg1area = models.BigIntegerField(blank=True, null=True)
    bdg1strycd = models.BigIntegerField(blank=True, null=True)
    ward = models.BigIntegerField(blank=True, null=True)
    policedist = models.BigIntegerField(blank=True, null=True)
    zip = models.BigIntegerField(blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True)
    neighborho = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    zoning = models.CharField(max_length=254, blank=True, null=True)
    sale = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    point_x = models.FloatField(blank=True, null=True)
    point_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StLouisCity_2022'

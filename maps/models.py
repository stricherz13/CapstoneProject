from django.db import models


class LRAModel(models.Model):
    handle = models.CharField(max_length=16, blank=True, null=True, db_index=True)
    updated = models.DateField(blank=True, null=True, db_index=True)
    siteaddr = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    ownername = models.CharField(max_length=37, blank=True, null=True, db_index=True)
    ownername2 = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    owneraddr = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    ownercity = models.CharField(max_length=13, blank=True, null=True, db_index=True)
    ownerstate = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    ownercntry = models.CharField(max_length=13, blank=True, null=True, db_index=True)
    ownerzip = models.CharField(max_length=9, blank=True, null=True, db_index=True)
    ownergroup = models.CharField(max_length=4, blank=True, null=True, db_index=True)
    numunits = models.IntegerField(blank=True, null=True, db_index=True)
    zoning1 = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    zoning2 = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    zoning3 = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    vacantland = models.CharField(max_length=1, blank=True, null=True, db_index=True)
    asmtland = models.BigIntegerField(blank=True, null=True, db_index=True)
    asmtimprov = models.BigIntegerField(blank=True, null=True, db_index=True)
    asmttotal = models.BigIntegerField(blank=True, null=True, db_index=True)
    landuse1 = models.IntegerField(blank=True, null=True, db_index=True)
    landuse2 = models.IntegerField(blank=True, null=True, db_index=True)
    landuse3 = models.IntegerField(blank=True, null=True, db_index=True)
    landuse4 = models.IntegerField(blank=True, null=True, db_index=True)
    asruse1 = models.IntegerField(blank=True, null=True, db_index=True)
    asruse2 = models.IntegerField(blank=True, null=True, db_index=True)
    asruse3 = models.IntegerField(blank=True, null=True, db_index=True)
    asruse4 = models.IntegerField(blank=True, null=True, db_index=True)
    asrclass1 = models.IntegerField(blank=True, null=True, db_index=True)
    asrclass2 = models.IntegerField(blank=True, null=True, db_index=True)
    asrclass3 = models.IntegerField(blank=True, null=True, db_index=True)
    asrclass4 = models.IntegerField(blank=True, null=True, db_index=True)
    legal1 = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    legal2 = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    legal3 = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    legal4 = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    legal5 = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    numbldgs = models.IntegerField(blank=True, null=True, db_index=True)
    landarea = models.IntegerField(blank=True, null=True, db_index=True)
    frontage = models.FloatField(blank=True, null=True, db_index=True)
    dailydate = models.DateField(blank=True, null=True, db_index=True)
    dailynum = models.CharField(max_length=7, blank=True, null=True, db_index=True)
    booknum = models.CharField(max_length=4, blank=True, null=True, db_index=True)
    bookpage = models.CharField(max_length=4, blank=True, null=True, db_index=True)
    bdg1year = models.IntegerField(blank=True, null=True, db_index=True)
    bdg1area = models.IntegerField(blank=True, null=True, db_index=True)
    bdg1exwall = models.IntegerField(blank=True, null=True, db_index=True)
    bdg1strycd = models.IntegerField(blank=True, null=True, db_index=True)
    bdg1occcd = models.IntegerField(blank=True, null=True, db_index=True)
    cityblock = models.FloatField(blank=True, null=True, db_index=True)
    parcel = models.FloatField(blank=True, null=True, db_index=True)
    parity = models.CharField(max_length=1, blank=True, null=True, db_index=True)
    addrnum = models.IntegerField(blank=True, null=True, db_index=True)
    addrsuf = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    streetpre = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    streetname = models.CharField(max_length=30, blank=True, null=True, db_index=True)
    streetsuf = models.CharField(max_length=4, blank=True, null=True, db_index=True)
    strsufdir = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    unitnum = models.CharField(max_length=10, blank=True, null=True, db_index=True)
    cdadist = models.IntegerField(blank=True, null=True, db_index=True)
    cdasubdist = models.IntegerField(blank=True, null=True, db_index=True)
    ward = models.IntegerField(blank=True, null=True, db_index=True)
    precinct02 = models.IntegerField(blank=True, null=True, db_index=True)
    precinct04 = models.IntegerField(blank=True, null=True, db_index=True)
    nbrhd = models.IntegerField(blank=True, null=True, db_index=True)
    asrnbrhd = models.IntegerField(blank=True, null=True, db_index=True)
    censblock = models.CharField(max_length=9, blank=True, null=True, db_index=True)
    policedist = models.IntegerField(blank=True, null=True, db_index=True)
    zip = models.CharField(max_length=5, blank=True, null=True, db_index=True)
    impactarea = models.IntegerField(blank=True, null=True, db_index=True)
    hsconserv = models.IntegerField(blank=True, null=True, db_index=True)
    ownerocc = models.CharField(max_length=1, blank=True, null=True, db_index=True)
    vacbldgyr = models.IntegerField(blank=True, null=True, db_index=True)
    parcel10 = models.BigIntegerField(blank=True, null=True, db_index=True)
    centract10 = models.FloatField(blank=True, null=True, db_index=True)
    cenblock10 = models.IntegerField(blank=True, null=True, db_index=True)
    ward10 = models.IntegerField(blank=True, null=True, db_index=True)
    precinct10 = models.IntegerField(blank=True, null=True, db_index=True)
    insparea10 = models.IntegerField(blank=True, null=True, db_index=True)
    leafarea = models.IntegerField(blank=True, null=True, db_index=True)
    blockpart = models.FloatField(blank=True, null=True, db_index=True)
    asrparcel = models.CharField(max_length=12, blank=True, null=True, db_index=True)
    centract20 = models.FloatField(blank=True, null=True, db_index=True)
    cenblock20 = models.IntegerField(blank=True, null=True, db_index=True)
    ward20 = models.IntegerField(blank=True, null=True, db_index=True)
    precinct20 = models.IntegerField(blank=True, null=True, db_index=True)
    insparea20 = models.IntegerField(blank=True, null=True, db_index=True)
    landuse = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    zoning = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    neighborho = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    point_x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_index=True)
    point_y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_index=True)

    class Meta:
        managed = False
        db_table = '2023_05_01_LRA'


class StLouisCityLandTax(models.Model):
    land_id = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    owner = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    address = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    total = models.FloatField(blank=True, null=True, db_index=True)
    handle = models.CharField(max_length=16, blank=True, null=True, db_index=True)
    numunits = models.BigIntegerField(blank=True, null=True, db_index=True)
    vacantland = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    numbldgs = models.BigIntegerField(blank=True, null=True, db_index=True)
    bdg1strycd = models.BigIntegerField(blank=True, null=True, db_index=True)
    ward = models.BigIntegerField(blank=True, null=True, db_index=True)
    policedist = models.BigIntegerField(blank=True, null=True, db_index=True)
    zip = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    landuse = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    neighborho = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    zoning = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    sale = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    point_x = models.FloatField(blank=True, null=True, db_index=True)
    point_y = models.FloatField(blank=True, null=True, db_index=True)

    class Meta:
        managed = False
        db_table = 'StLouisCity_2022'


class StLouisCityLandTaxModel2023(models.Model):
    sale = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    landtaxid = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    address = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    total = models.FloatField(blank=True, null=True, db_index=True)
    handle = models.CharField(max_length=16, blank=True, null=True, db_index=True)
    updated = models.DateField(blank=True, null=True)
    siteaddr = models.CharField(max_length=40, blank=True, null=True, db_index=True)
    ownername = models.CharField(max_length=37, blank=True, null=True)
    ownername2 = models.CharField(max_length=40, blank=True, null=True)
    owneraddr = models.CharField(max_length=40, blank=True, null=True)
    ownercity = models.CharField(max_length=13, blank=True, null=True)
    ownerstate = models.CharField(max_length=2, blank=True, null=True)
    ownercntry = models.CharField(max_length=13, blank=True, null=True)
    ownerzip = models.CharField(max_length=9, blank=True, null=True)
    ownergroup = models.CharField(max_length=4, blank=True, null=True)
    numunits = models.IntegerField(blank=True, null=True, db_index=True)
    zoning1 = models.CharField(max_length=2, blank=True, null=True)
    zoning2 = models.CharField(max_length=2, blank=True, null=True)
    zoning3 = models.CharField(max_length=2, blank=True, null=True)
    vacantland = models.CharField(max_length=1, blank=True, null=True, db_index=True)
    asmtland = models.BigIntegerField(blank=True, null=True)
    asmtimprov = models.BigIntegerField(blank=True, null=True)
    asmttotal = models.BigIntegerField(blank=True, null=True)
    landuse1 = models.IntegerField(blank=True, null=True)
    landuse2 = models.IntegerField(blank=True, null=True)
    landuse3 = models.IntegerField(blank=True, null=True)
    landuse4 = models.IntegerField(blank=True, null=True)
    asruse1 = models.IntegerField(blank=True, null=True)
    asruse2 = models.IntegerField(blank=True, null=True)
    asruse3 = models.IntegerField(blank=True, null=True)
    asruse4 = models.IntegerField(blank=True, null=True)
    asrclass1 = models.IntegerField(blank=True, null=True)
    asrclass2 = models.IntegerField(blank=True, null=True)
    asrclass3 = models.IntegerField(blank=True, null=True)
    asrclass4 = models.IntegerField(blank=True, null=True)
    legal1 = models.CharField(max_length=40, blank=True, null=True)
    legal2 = models.CharField(max_length=40, blank=True, null=True)
    legal3 = models.CharField(max_length=40, blank=True, null=True)
    legal4 = models.CharField(max_length=40, blank=True, null=True)
    legal5 = models.CharField(max_length=40, blank=True, null=True)
    numbldgs = models.IntegerField(blank=True, null=True, db_index=True)
    landarea = models.BigIntegerField(blank=True, null=True)
    frontage = models.FloatField(blank=True, null=True)
    dailydate = models.DateField(blank=True, null=True)
    dailynum = models.CharField(max_length=7, blank=True, null=True)
    booknum = models.CharField(max_length=4, blank=True, null=True)
    bookpage = models.CharField(max_length=4, blank=True, null=True)
    bdg1year = models.IntegerField(blank=True, null=True)
    bdg1area = models.BigIntegerField(blank=True, null=True)
    bdg1exwall = models.IntegerField(blank=True, null=True)
    bdg1strycd = models.IntegerField(blank=True, null=True)
    bdg1occcd = models.IntegerField(blank=True, null=True)
    cityblock = models.FloatField(blank=True, null=True)
    parcel = models.FloatField(blank=True, null=True)
    parity = models.CharField(max_length=1, blank=True, null=True)
    addrnum = models.BigIntegerField(blank=True, null=True)
    addrsuf = models.CharField(max_length=2, blank=True, null=True)
    streetpre = models.CharField(max_length=2, blank=True, null=True)
    streetname = models.CharField(max_length=30, blank=True, null=True)
    streetsuf = models.CharField(max_length=4, blank=True, null=True)
    strsufdir = models.CharField(max_length=2, blank=True, null=True)
    unitnum = models.CharField(max_length=10, blank=True, null=True)
    cdadist = models.IntegerField(blank=True, null=True)
    cdasubdist = models.IntegerField(blank=True, null=True)
    ward = models.IntegerField(blank=True, null=True)
    precinct02 = models.IntegerField(blank=True, null=True)
    precinct04 = models.IntegerField(blank=True, null=True)
    nbrhd = models.IntegerField(blank=True, null=True)
    asrnbrhd = models.IntegerField(blank=True, null=True)
    censblock = models.CharField(max_length=9, blank=True, null=True)
    policedist = models.BigIntegerField(blank=True, null=True, db_index=True)
    zip = models.BigIntegerField(blank=True, null=True, db_index=True)
    impactarea = models.IntegerField(blank=True, null=True)
    hsconserv = models.IntegerField(blank=True, null=True)
    ownerocc = models.CharField(max_length=1, blank=True, null=True)
    vacbldgyr = models.IntegerField(blank=True, null=True)
    centract10 = models.FloatField(blank=True, null=True)
    cenblock10 = models.IntegerField(blank=True, null=True)
    ward10 = models.IntegerField(blank=True, null=True)
    insparea10 = models.IntegerField(blank=True, null=True)
    leafarea = models.IntegerField(blank=True, null=True)
    blockpart = models.FloatField(blank=True, null=True)
    asrparcel = models.CharField(max_length=12, blank=True, null=True)
    centract20 = models.FloatField(blank=True, null=True)
    cenblock20 = models.IntegerField(blank=True, null=True)
    ward20 = models.IntegerField(blank=True, null=True, db_index=True)
    precinct20 = models.IntegerField(blank=True, null=True)
    insparea20 = models.IntegerField(blank=True, null=True)
    landuse = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    zoning = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    neighborho = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    point_x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_index=True)
    point_y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_index=True)

    class Meta:
        managed = False
        db_table = 'stlouiscity2023'

class StCharles2023Model(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    parcel_id = models.CharField(max_length=27, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    siteaddres = models.CharField(max_length=36, blank=True, null=True)
    mailingadd = models.CharField(max_length=69, blank=True, null=True)
    proptype = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    municipali = models.CharField(max_length=29, blank=True, null=True, db_index=True)
    firedistri = models.CharField(max_length=26, blank=True, null=True, db_index=True)
    schooldist = models.CharField(max_length=14, blank=True, null=True, db_index=True)
    nbhdcode = models.CharField(max_length=4, blank=True, null=True)
    qualcode = models.CharField(max_length=2, blank=True, null=True)
    legal = models.CharField(max_length=147, blank=True, null=True)
    subdivisio = models.CharField(max_length=89, blank=True, null=True)
    situsnumbe = models.CharField(max_length=5, blank=True, null=True)
    situsname = models.CharField(max_length=31, blank=True, null=True)
    situszip = models.CharField(max_length=5, blank=True, null=True, db_index=True)
    lotnumber = models.CharField(max_length=4, blank=True, null=True)
    lotsplit = models.CharField(max_length=7, blank=True, null=True)
    lotsize = models.CharField(max_length=15, blank=True, null=True)
    yearbuilt = models.CharField(max_length=4, blank=True, null=True)
    basearea = models.IntegerField(blank=True, null=True)
    totalarea = models.IntegerField(blank=True, null=True)
    totalmarke = models.IntegerField(blank=True, null=True)
    residentia = models.IntegerField(blank=True, null=True)
    resident_1 = models.IntegerField(blank=True, null=True)
    resident_2 = models.IntegerField(blank=True, null=True)
    commercial = models.IntegerField(blank=True, null=True)
    commerci_1 = models.IntegerField(blank=True, null=True)
    commerci_2 = models.IntegerField(blank=True, null=True)
    agricultur = models.IntegerField(blank=True, null=True)
    agricult_1 = models.IntegerField(blank=True, null=True)
    agricult_2 = models.IntegerField(blank=True, null=True)
    tifdistric = models.CharField(max_length=29, blank=True, null=True)
    style = models.CharField(max_length=49, blank=True, null=True)
    archtype = models.CharField(max_length=3, blank=True, null=True)
    occcode = models.CharField(max_length=4, blank=True, null=True)
    bedrooms = models.CharField(max_length=5, blank=True, null=True, db_index=True)
    bathrooms = models.CharField(max_length=5, blank=True, null=True, db_index=True)
    halfbathro = models.CharField(max_length=4, blank=True, null=True, db_index=True)
    totalrooms = models.CharField(max_length=5, blank=True, null=True)
    exteriorwa = models.CharField(max_length=46, blank=True, null=True)
    garagestal = models.CharField(max_length=5, blank=True, null=True, db_index=True)
    prevowner1 = models.CharField(max_length=100, blank=True, null=True)
    salecode1 = models.CharField(max_length=1, blank=True, null=True)
    saleprice1 = models.IntegerField(blank=True, null=True)
    saledate1 = models.DateField(blank=True, null=True)
    bookpage1 = models.CharField(max_length=12, blank=True, null=True)
    prevowner2 = models.CharField(max_length=100, blank=True, null=True)
    salecode2 = models.CharField(max_length=1, blank=True, null=True)
    saleprice2 = models.IntegerField(blank=True, null=True)
    saledate2 = models.DateField(blank=True, null=True)
    bookpage2 = models.CharField(max_length=12, blank=True, null=True)
    prevowner3 = models.CharField(max_length=100, blank=True, null=True)
    salecode3 = models.CharField(max_length=1, blank=True, null=True)
    saleprice3 = models.IntegerField(blank=True, null=True)
    saledate3 = models.DateField(blank=True, null=True)
    bookpage3 = models.CharField(max_length=12, blank=True, null=True)
    prevowner4 = models.CharField(max_length=99, blank=True, null=True)
    salecode4 = models.CharField(max_length=1, blank=True, null=True)
    saleprice4 = models.IntegerField(blank=True, null=True)
    saledate4 = models.DateField(blank=True, null=True)
    bookpage4 = models.CharField(max_length=12, blank=True, null=True)
    sketch = models.CharField(max_length=53, blank=True, null=True, db_index=True)
    parcelrepo = models.CharField(max_length=58, blank=True, null=True, db_index=True)
    parcel_sta = models.CharField(max_length=2, blank=True, null=True)
    glink = models.CharField(max_length=67, blank=True, null=True, db_index=True)
    parcel_acr = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True, db_index=True)
    total = models.FloatField(blank=True, null=True, db_index=True)
    point_x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_index=True)
    point_y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True, db_index=True)

    class Meta:
        managed = False
        db_table = 'StCharles2023'

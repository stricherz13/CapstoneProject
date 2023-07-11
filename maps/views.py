import folium
from django.shortcuts import render
from .models import StLouisCityLandTax, LRAModel, StLouisCityLandTaxModel2023
from .forms import StLouisCityLandTaxForm, LRAForm, StLouisCityLandTaxForm2023


def formViewPage(request):
    properties = StLouisCityLandTax.objects.all()
    if request.method == 'GET' and len(request.GET):
        form = StLouisCityLandTaxForm(request.GET)
        if form.is_valid():
            sale = form.cleaned_data['sale']
            neighborho = form.cleaned_data['neighborho']
            landuse = form.cleaned_data['landuse']
            zoning = form.cleaned_data['zoning']
            policedist = form.cleaned_data['policedist']
            zip = form.cleaned_data['zip']
            if sale:
                properties = properties.filter(sale__in=sale)
            if neighborho:
                properties = properties.filter(neighborho__in=neighborho)
            if landuse:
                properties = properties.filter(landuse__in=landuse)
            if zoning:
                properties = properties.filter(zoning__in=zoning)
            if policedist:
                properties = properties.filter(policedist__in=policedist)
            if zip:
                properties = properties.filter(zip__in=zip)
    else:
        form = StLouisCityLandTaxForm()

    context = {'form': form, 'properties': properties}

    return context


def foliumMap(properties):
    # create a Folium map centered on St Louis
    m = folium.Map(location=[38.627003, -90.199402], zoom_start=11, prefer_canvas=True)

    # add tile layer control and tile layer
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
        overlay=False,
        control=True
    ).add_to(m)
    folium.LayerControl().add_to(m)

    # add markers to the map for each station
    for i in properties:
        coordinates = (i.point_y, i.point_x)
        iframe = folium.IFrame(
            f"Land tax ID: {i.land_id}" + '<br>' + f"Owner: {i.owner}" + '<br>' + f"Address: {i.address}" + '<br>' +
            f"Total: {i.total}" + '<br>' + f"<a href = https://dynamic.stlouis-mo.gov/citydata/newdesign/data.cfm?Handle={i.handle} target = _blank > Geo St.Louis Link </a>")
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(coordinates, popup=popup, icon=folium.Icon(prefix='fa', icon='circle', color='blue')).add_to(m)

    context = {'map': m._repr_html_()}
    return context


def tablePage(properties):
    context = {'table': properties}
    return context


def combinedView(request):
    form = formViewPage(request)
    m = foliumMap(form['properties'])
    table = tablePage(form['properties'])

    context = {
        'form': form['form'],
        'map': m['map'],
        'table': table['table']
    }
    return render(request, 'maps/StLouisCityLandTaxSale.html', context)


def LRAformViewPage(request):
    properties = LRAModel.objects.all()
    if request.method == 'GET' and len(request.GET):
        form = LRAForm(request.GET)
        if form.is_valid():
            neighborho = form.cleaned_data['neighborho']
            ward20 = form.cleaned_data['ward20']
            vacantland = form.cleaned_data['vacantland']
            landuse = form.cleaned_data['landuse']
            zoning = form.cleaned_data['zoning']
            policedist = form.cleaned_data['policedist']
            zip = form.cleaned_data['zip']
            if neighborho:
                properties = properties.filter(neighborho__in=neighborho)
            if ward20:
                properties = properties.filter(ward20__in=ward20)
            if vacantland:
                properties = properties.filter(vacantland__in=vacantland)
            if landuse:
                properties = properties.filter(landuse__in=landuse)
            if zoning:
                properties = properties.filter(zoning__in=zoning)
            if policedist:
                properties = properties.filter(policedist__in=policedist)
            if zip:
                properties = properties.filter(zip__in=zip)
    else:
        form = LRAForm()

    context = {'LRAform': form, 'LRAproperties': properties}

    return context


def LRAfoliumMap(LRAproperties):
    # create a Folium map centered on St Louis
    m = folium.Map(location=[38.627003, -90.199402], zoom_start=11, prefer_canvas=True)

    # add tile layer control and tile layer
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
        overlay=False,
        control=True
    ).add_to(m)
    folium.LayerControl().add_to(m)

    # add markers to the map for each station
    for i in LRAproperties:
        coordinates = (i.point_y, i.point_x)
        iframe = folium.IFrame(
            f"Handle: {i.handle}" + '<br>' + f"Address: {i.siteaddr}" + '<br>' + f"Ward: {i.ward20}" + '<br>' + f"Vacant lot: {i.vacantland}" + '<br>' +
            f"Units: {i.numunits}" + '<br>' + f"Buildings: {i.numbldgs}" + '<br>' + f"Neighborbood: {i.neighborho}" + '<br>' + f"Land use: {i.landuse}" + '<br>' +
            f"Zoning: {i.zoning}" + '<br>' + f"<a href =https://dynamic.stlouis-mo.gov/citydata/newdesign/data.cfm?Handle={i.handle} target=_blank>Geo St.Louis Link</a>")
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(coordinates, popup=popup, icon=folium.Icon(prefix='fa', icon='circle', color='blue')).add_to(m)

    context = {'LRAmap': m._repr_html_()}
    return context


def LRAtablePage(LRAproperties):
    context = {'LRAtable': LRAproperties}
    return context


def LRAcombinedView(request):
    form = LRAformViewPage(request)
    m = LRAfoliumMap(form['LRAproperties'])
    table = LRAtablePage(form['LRAproperties'])

    context = {
        'form': form['LRAform'],
        'map': m['LRAmap'],
        'table': table['LRAtable']
    }
    return render(request, 'maps/LRAMap.html', context)


def formViewPageSTL2023(request):
    properties = StLouisCityLandTaxModel2023.objects.all()
    if request.method == 'GET' and len(request.GET):
        form = StLouisCityLandTaxForm2023(request.GET)
        if form.is_valid():
            sale = form.cleaned_data['sale']
            neighborho = form.cleaned_data['neighborho']
            policedist = form.cleaned_data['policedist']
            zip = form.cleaned_data['zip']
            ward = form.cleaned_data['ward']
            landuse = form.cleaned_data['landuse']
            zoning = form.cleaned_data['zoning']
            numunits = form.cleaned_data['numunits']
            vacantland = form.cleaned_data['vacantland']
            numbldgs = form.cleaned_data['numbldgs']

            if sale:
                properties = properties.filter(sale__in=sale)
            if neighborho:
                properties = properties.filter(neighborho__in=neighborho)
            if policedist:
                properties = properties.filter(policedist__in=policedist)
            if zip:
                properties = properties.filter(zip__in=zip)
            if ward:
                properties = properties.filter(ward__in=ward)
            if landuse:
                properties = properties.filter(landuse__in=landuse)
            if zoning:
                properties = properties.filter(zoning__in=zoning)
            if numunits:
                properties = properties.filter(numunits__in=numunits)
            if vacantland:
                properties = properties.filter(vacantland__in=vacantland)
            if numbldgs:
                properties = properties.filter(numbldgs__in=numbldgs)
    else:
        form = StLouisCityLandTaxForm2023()

    context = {'form': form, 'propertiesSTL2023': properties}

    return context


def foliumMapSTL2023(propertiesSTL2023):
    # create a Folium map centered on St Louis
    m = folium.Map(location=[38.627003, -90.199402], zoom_start=12, prefer_canvas=True)

    # add tile layer control and tile layer
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
        overlay=False,
        control=True
    ).add_to(m)
    folium.LayerControl().add_to(m)

    # add markers to the map for each station
    for i in propertiesSTL2023:
        coordinates = (i.point_y, i.point_x)
        iframe = folium.IFrame(
            f"Land Tax ID: {i.landtaxid}" + '<br>' + f"Owner: {i.ownername}" + '<br>' + f"Address: {i.address}" + '<br>' + f"Total: {i.total}" + '<br>' +
            f"Neighborhood: {i.neighborho}" + '<br>' + f"Ward: {i.ward20}" + '<br>' + f"Land Use: {i.landuse}" + '<br>' + f"Zoning: {i.zoning}" + '<br>' +
            f"Vacant lot: {i.vacantland}" + '<br>' + f"<a href =https://dynamic.stlouis-mo.gov/citydata/newdesign/data.cfm?Handle={i.handle} target=_blank>Geo St.Louis Link</a>")
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(coordinates, popup=popup, icon=folium.Icon(prefix='fa', icon='circle', color='blue')).add_to(m)

    context = {'mapSTL2023': m._repr_html_()}
    return context


def tablePageSTL2023(propertiesSTL2023):
    context = {'tableSTL2023': propertiesSTL2023}
    return context


def combinedViewSTL2023(request):
    form = formViewPageSTL2023(request)
    m = foliumMapSTL2023(form['propertiesSTL2023'])
    table = tablePageSTL2023(form['propertiesSTL2023'])

    context = {
        'form': form['form'],
        'map': m['mapSTL2023'],
        'table': table['tableSTL2023']
    }
    return render(request, 'maps/StLouisCityLandTaxSale2023.html', context)

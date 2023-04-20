import folium
from django.shortcuts import render
from .models import StLouisCityLandTax
from .forms import StLouisCityLandTaxForm


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
    m = folium.Map(location=[38.627003, -90.199402], zoom_start=11)

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


# def tablePage(properties):
#     context = {'':}
#     return context


def combinedView(request):
    form = formViewPage(request)
    m = foliumMap(form['properties'])

    context = {
        'form': form['form'],
        'map': m['map']
    }
    return render(request, 'maps/StLouisCityLandTaxSale.html', context)

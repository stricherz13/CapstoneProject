import folium
from django.shortcuts import render
from .utils import *
from .models import StLouisCityLandTax
from .forms import StLouisCityLandTaxForm


def formViewPage(request):
    if request.method == 'GET':
        form = StLouisCityLandTaxForm(request.GET)
        if form.is_valid():
            sale = form.cleaned_data['sale']
            neighborho = form.cleaned_data['neighborho']
            properties = StLouisCityLandTax.objects.filter(sale__in=sale,
                                                           neighborho__in=neighborho)
        else:
            properties = StLouisCityLandTax.objects.all()
    else:
        form = StLouisCityLandTaxForm()
        properties = StLouisCityLandTax.objects.all()

    context = {'form': form, 'properties': properties}

    return render(request, 'maps/partials/_form.html', context)


def foliumMap(request):
    properties = StLouisCityLandTax.objects.all()

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
        # folium.Marker(coordinates).add_to(m)
        iframe = folium.IFrame(
            f"Land tax ID: {i.land_id}" + '<br>' + f"Owner: {i.owner}" + '<br>' + f"Address: {i.address}" + '<br>' +
            f"Total: {i.total}" + '<br>' + f"<a href = https://dynamic.stlouis-mo.gov/citydata/newdesign/data.cfm?Handle={i.handle} target = _blank > Geo St.Louis Link </a>")
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(coordinates, popup=popup, icon=folium.Icon(prefix='fa', icon='circle', color='blue')).add_to(m)

    context = {'map': m._repr_html_()}

    return render(request, 'maps/partials/_map.html', context)


# def tablePage(request):
#
#     return render(request, 'maps/partials/_table.html')


def combinedView(request):
    form = formViewPage(request)
    m = foliumMap(request)


    context = {
        'form': form,
        'map': m._repr_html_(),
    }
    return render(request, 'maps/StLouisCityLandTaxSale.html', context)

import folium
from .models import StLouisCityLandTax
from .forms import StLouisCityLandTaxForm


# def formViewFunction(request):
#     if request.method == 'GET':
#         form = StLouisCityLandTaxForm(request.get)
#         if form.is_valid():
#             sale = form.cleaned_data['sale']
#             neighborho = form.cleaned_data['neighborho']
#             properties = StLouisCityLandTax.objects.filter(sale=sale, neighborho=neighborho)
#         else:
#             properties = StLouisCityLandTax.objects.all()
#
#     else:
#         form = StLouisCityLandTaxForm()
#         properties = StLouisCityLandTax.objects.all()
#
#     return form, properties


def mapFunction():
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
            f"Total: {i.total}" + '<br>' + f"<a href = https://dynamic.stlouis-mo.gov/citydata/newdesign/data.cfm?Handle={i.handle} target = _blank > Geo St.Louis Link </a>" + '<br>' + {i.address})
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(coordinates, popup=popup, icon=folium.Icon(prefix='fa', icon='circle', color='blue')).add_to(m)

    return m

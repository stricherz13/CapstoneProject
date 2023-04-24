// map
var map = L.map('map').setView([38.637, -90.199], 12);
var imagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}').addTo(map);
var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Layer controller
var baselayers = {
  "Imagery": imagery,
  "Map": osm,
};

L.control.layers(baselayers).addTo(map)

//Geoserver Web Feature Service
$.ajax('http://localhost:8080/geoserver/wfs',{
  type: 'GET',
  data: {
    service: 'WFS',
    version: '1.1.0',
    request: 'GetFeature',
    typename: 'STLTaxAuctionMap:STL_CIty_Sample_Data_Points',
    srsname: 'EPSG:4326',
    outputFormat: 'text/javascript',
    },
  dataType: 'jsonp',
  jsonpCallback:'callback:handleJson',
  jsonp:'format_options'
 });
  
 //Geojson style file
  var myStyle = {
    'color': 'red'
  }

  // the ajax callback function
function handleJson(data) {
    selectedArea = L.geoJson(data, {
      style: myStyle,
      onEachFeature: function(feature, layer) {
        layer.bindPopup(`Name: ${feature.properties.name_of_your_property}`)
      }
    }).addTo(map);
  map.fitBounds(selectedArea.getBounds());
}
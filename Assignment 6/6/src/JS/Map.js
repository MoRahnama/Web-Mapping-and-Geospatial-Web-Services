// define osm layer -- basemap1
	var osmmap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	});

// define esri layer -- basemap 2
var esrimap = L.esri.basemapLayer("Topographic");

// define topomap layer -- basemap3

var topomap = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	maxZoom: 17,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});

var mymap = L.map('mapid', {
	center: [47.65, -65.45],
	zoom: 10,
	layers: [osmmap, esrimap, topomap]
});

// Overlays 

var canvec1 = L.tileLayer.wms("http://gaia.gge.unb.ca:8080/cgi-bin/mapserv.exe?map=/ms4w/Apache/htdocs/gge5403/students/mohammadali/6/src/map/Gloucester_wms.map", {
	layers: 'RoadSegments',
	format: 'image/png',
	transparent: true,
	attribution: "GGE5403, CanVec"
});

var canvec2 = L.tileLayer.wms("http://gaia.gge.unb.ca:8080/cgi-bin/mapserv.exe?map=/ms4w/Apache/htdocs/gge5403/students/mohammadali/6/src/map/Gloucester_wms.map", {
	layers: 'RoadJunction',
	format: 'image/png',
	transparent: true,
	attribution: "GGE5403, CanVec"
});

var module5 = L.tileLayer.wms("http://gaia.gge.unb.ca:8080/cgi-bin/mapserv.exe?map=/ms4w/Apache/htdocs/gge5403/students/mohammadali/6/src/map/Gloucester_wms.map", {
	layers: 'WaterBody',
	format: 'image/png',
	transparent: true,
	attribution: "GGE5403, CanVec"
});

var baseLayers = {
	"OSM": osmmap,
	"ESRI": esrimap,
	"TOPO": topomap
};

var overlays = {
	"RoadSegments": canvec1,
	"RoadJunction": canvec2,
	"WaterBody": module5
};

L.control.layers(baseLayers, overlays).addTo(mymap);

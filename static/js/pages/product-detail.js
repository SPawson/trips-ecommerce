var mapEl = document.getElementById("location-map");
var lat = parseFloat(mapEl.dataset.lat);
var long = parseFloat(mapEl.dataset.long);

function initMap() {
    var map = new google.maps.Map(mapEl, {
        zoom: 14,
        center: {
            lat: lat,
            lng: long
        }
    });

    var labels = "ABCDEFGHIJKLMONPQRSTUVWXYZ";

    var locations = [{
        lat: lat,
        lng: long
    }];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, {
        imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
    });
}





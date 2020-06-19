var mapEl = document.getElementById("location-map");
var readMore = document.getElementById("read-more");
var snippet = document.getElementById("snippet");
var fullDesc = document.getElementById("full-description");
var likeInput = document.getElementById("id_like");
var likeBtn = document.getElementById("like-button");


if(mapEl != null){
    var lat = parseFloat(mapEl.dataset.lat);
    var long = parseFloat(mapEl.dataset.long);
}
else {
    var lat = 53.8008;
    var long = -1.5491;
}

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

readMore.addEventListener("click", function(){

    let state = readMore.dataset.state;

    if (state == "more") {
        snippet.classList.add("hidden");
        fullDesc.classList.remove("hidden");
        readMore.innerHTML = "Read Less";
        readMore.setAttribute("data-state", "less");
    }
    else if (state == "less") {
        fullDesc.classList.add("hidden");
        snippet.classList.remove("hidden");
        readMore.innerHTML = "Read More";
        window.scrollTo(0,80);
        readMore.setAttribute("data-state", "more");
    }

});

likeBtn.addEventListener("click", function(){
 
    let state = likeBtn.dataset.state;

    if (state == "unliked") {
        likeBtn.classList.add("liked");
        likeBtn.setAttribute("data-state", "liked");
        likeInput.checked = true;
    }
    else if (state == "liked") {
        likeBtn.classList.remove("liked");
        likeBtn.setAttribute("data-state", "unliked");
        likeInput.checked = false;
    }
});



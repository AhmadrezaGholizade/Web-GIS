
const osmLayer = new ol.layer.Tile({
    source: new ol.source.OSM(),
})

const rashtBase = new ol.layer.Tile({
    source: new ol.source.TileWMS({
        url: 'http://localhost:8080/geoserver/rasht/wms',
        params: {
            'LAYERS': 'rashtBaseMap',
            'TILED': true
        },
    })
})

const map = new ol.Map({
  layers: [
    osmLayer, rashtBase
  ],
  target: 'map',
  view: new ol.View({
    center: ol.proj.fromLonLat([49.58, 37.24]),
    zoom: 12,
  }),
});



document.getElementById('overlayButton').onclick = function () {
    var overlayDiv = document.getElementById('overlayDiv');
    // Toggle the display property
    if (overlayDiv.style.display === 'block') {
        overlayDiv.style.display = 'none';
    } else {
        overlayDiv.style.display = 'block';
    }
};


const osmCheckbox = document.getElementById('osmCheckbox');
const rashtCheckbox = document.getElementById('rashtCheckbox');

// Function to handle checkbox click events
function handleCheckboxClick(event) {
  const checkbox = event.target;  // Get the clicked checkbox element
  const isChecked = checkbox.checked;  // Check if it's checked

  if (checkbox === osmCheckbox) {
    // Code to execute when OSM checkbox is clicked (e.g., toggle map layer visibility)
    if (isChecked){
        map.getLayers().insertAt(0, osmLayer); 

    }else{
        map.removeLayer(osmLayer)
    }
    console.log(map.layers)
  } else if (checkbox === rashtCheckbox) {
    // Code to execute when Rasht Base checkbox is clicked (e.g., toggle map overlay)
    if (isChecked){
        map.addLayer(rashtBase)
    }else{
        map.removeLayer(rashtBase)
    }
    console.log(map.layers)
  }
}

// Add event listeners to both checkboxes
osmCheckbox.addEventListener('click', handleCheckboxClick);
rashtCheckbox.addEventListener('click', handleCheckboxClick);



// import MVT from 'ol/format/MVT.js';
// import Map from 'ol/Map.js';
// import VectorTileLayer from 'ol/layer/VectorTile.js';
// import VectorTileSource from 'ol/source/VectorTile.js';
// import View from 'ol/View.js';
// import {Fill, Stroke, Style} from 'ol/style.js';

var wmtsSource = new ol.source.WMTS({
  url: 'http://localhost:8080/geoserver/opengeo/gwc/service/wmts',
  layer: 'opengeo:ne_110m_admin_0_countries',
  matrixSet: 'EPSG:4326',
  format: 'application/json;type=geojson',
  tileGrid: new ol.tilegrid.WMTS({
      tileSize: [256, 256],
      origin: [-180, 90],
      resolutions: [
          0.703125, 0.3515625, 0.17578125, 0.087890625, 0.0439453125, 
          0.02197265625, 0.010986328125, 0.0054931640625, 0.00274658203125,
          0.001373291015625, 0.0006866455078125, 0.00034332275390625,
          0.000171661376953125, 0.0000858306884765625, 0.00004291534423828125,
          0.000021457672119140625, 0.0000107288360595703125, 0.000005364418029785156
      ],
      matrixIds: [
          'EPSG:4326:0', 'EPSG:4326:1', 'EPSG:4326:2', 'EPSG:4326:3', 
          'EPSG:4326:4', 'EPSG:4326:5', 'EPSG:4326:6', 'EPSG:4326:7', 
          'EPSG:4326:8', 'EPSG:4326:9', 'EPSG:4326:10', 'EPSG:4326:11', 
          'EPSG:4326:12', 'EPSG:4326:13', 'EPSG:4326:14', 'EPSG:4326:15', 
          'EPSG:4326:16', 'EPSG:4326:17'
      ]
  })
});

// Create the WMTS layer
var wmtsLayer = new ol.layer.Tile({
  source: wmtsSource
});

// // Create the map
// var map = new ol.Map({
//   target: 'map', // Replace 'map' with the id of your map div
//   layers: [wmtsLayer],
//   view: new ol.View({
//       center: [0, 0], // Set your desired center coordinates
//       zoom: 2 // Set your desired initial zoom level
//   })
// });

const map = new ol.Map({
  layers: [wmtsLayer],
  target: 'map',
  view: new ol.View({
    center: [0, 0],
    zoom: 2,
    multiWorld: true,
  }),
});

// // Selection
// const selectionLayer = new ol.layer.Vector({
//   map: map,
//   renderMode: 'vector',
//   source: vtLayer.getSource(),
//   style: function (feature) {
//     if (feature.getId() in selection) {
//       return selectedCountry;
//     }
//   },
// });

// const selectElement = document.getElementById('type');

// map.on(['click', 'pointermove'], function (event) {
//   if (
//     (selectElement.value === 'singleselect-hover' &&
//       event.type !== 'pointermove') ||
//     (selectElement.value !== 'singleselect-hover' &&
//       event.type === 'pointermove')
//   ) {
//     return;
//   }
//   vtLayer.getFeatures(event.pixel).then(function (features) {
//     if (!features.length) {
//       selection = {};
//       selectionLayer.changed();
//       return;
//     }
//     const feature = features[0];
//     if (!feature) {
//       return;
//     }
//     const fid = feature.getId();

//     if (selectElement.value.startsWith('singleselect')) {
//       selection = {};
//     }
//     // add selected feature to lookup
//     selection[fid] = feature;

//     selectionLayer.changed();
//   });
// });


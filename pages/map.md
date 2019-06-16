---
layout: page
title: Map
description: Where are clusters on the map?
permalink: /map/
---

<style>
#map-container {
  height: 500px;
  margin:0 auto;
  max-width:1240px;
}
.page-heading {
    padding-bottom: 10px !important;
}
.container {
   max-width: 1440px;
}
.css-icon {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #00b388;
}
</style>

<p style='text-align:center'>Don't see your center or resource here? <a href="https://www.github.com/hpsee/top" target="_blank">Add it to the map!</a>
</p>

<div id="map-container" style="height:800px"></div>

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
      integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
      crossorigin=""/>

<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
     integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
     crossorigin=""></script>

{% include map.html %}

<br/>
<br/>
Map made with [leafletjs](http://leafletjs.com), and [Open Streetmap](https://osm.org/).

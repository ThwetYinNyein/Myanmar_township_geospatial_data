# 🗺️ Myanmar Township Area Extractor with Python

This project extracts township-level geospatial information from MIMU (Myanmar Information Management Unit), calculates the area of each township using proper map projection, and convert the geometry boundry points to a pair of longitude and lattitude.

---
## 🛠️ Resources
https://geonode.themimu.info/layers/?limit=100&offset=0

## 📌 Features

- Reads township boundaries from a GeoJSON file (`township_geo.geojson`)
- Calculates accurate township areas in square kilometers
- Extracts township name, code, centroid (lat/lon), and area
- Exports the results to CSV

---

## 🛠️ Technologies Used

- Python 3
- [GeoPandas](https://geopandas.org/) – for geospatial processing
- [PostGIS (optional)](https://postgis.net/) – if you want to store geometries

---
Thank You.



import geopandas as gpd
import pandas as pd

# Load GeoJSON file
gdf = gpd.read_file("township_geo.geojson")

# Reproject to UTM (e.g., EPSG:32646 for Myanmar zone 46N)
gdf_utm = gdf.to_crs(epsg=32646)

# Calculate area in square kilometers
gdf['area_km2'] = gdf_utm.area / 10**6

# Calculate centroid in projected CRS, then convert back to lat/lon
centroids = gdf_utm.centroid.to_crs(epsg=4326)
gdf['lat'] = centroids.y
gdf['lon'] = centroids.x


# Select relevant columns
output_df = gdf[['TS', 'TS_PCODE', 'lat', 'lon', 'area_km2']]
output_df.columns = ['Township_Name', 'Township_Code', 'Latitude', 'Longitude', 'Area_km2']

# Save to CSV
output_df.to_csv("township_summary.csv", index=False)

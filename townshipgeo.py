import geopandas as gpd

# Load GeoJSON file
gdf = gpd.read_file('township_geo.geojson')

# Print all columns to confirm field names
print(gdf.columns)

# Extract needed columns (TS: township name, TS_PCODE: code, geometry)
gdf = gdf[['TS', 'TS_PCODE', 'geometry']]

# Project to metric CRS for area calculation (UTM Zone 46N for Myanmar)
gdf = gdf.to_crs(epsg=32646)

# Calculate area in square kilometers
gdf['area_sqkm'] = gdf['geometry'].area / 1e6

# Rename columns for clarity
gdf = gdf.rename(columns={'TS': 'Township_Name', 'TS_PCODE': 'Township_Code'})

# Convert geometry to WKT format
gdf['geometry_wkt'] = gdf['geometry'].apply(lambda geom: geom.wkt)

# Save to CSV with geometry in WKT
gdf[['Township_Name', 'Township_Code', 'area_sqkm', 'geometry_wkt']].to_csv('township_areas_with_geometry.csv', index=False)

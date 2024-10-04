import osmnx as ox
import geopandas as gpd

# Define the place to extract data from (Victoria, Australia)
place_name = "Victoria, Australia"

# Create a dictionary for the tags, filtering for grocery-related places
tags = {'shop': ['grocery', 'supermarket']}

# Use osmnx to download POI data that matches the tags
gdf = ox.geometries_from_place(place_name, tags)

# Display the first few rows of the data
print(gdf.head())

# Save the data to a GeoJSON or CSV file for further analysis
gdf.to_file("../data/raw/grocery_markets_victoria.geojson", driver='GeoJSON')

columns_of_interest = ['name', 'shop', 'addr:street', 'geometry']

gdf_filtered = gdf[columns_of_interest]

# Filter out rows with missing values
gdf_filtered = gdf_filtered.dropna()

gdf_filtered.to_csv("../data/raw/grocery_markets_victoria.csv", index=False)
gdf_filtered.head()
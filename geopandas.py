import folium

# Define map center and zoom level
lat = 51.505
lon = -0.09

# Create map object
m=folium.Map(location=[lat, lon], zoom_start=13)

# Add markers
folium.Marker(location=[lat, lon], popup="This is a marker!").add_to(m)

# Display map
print(m)


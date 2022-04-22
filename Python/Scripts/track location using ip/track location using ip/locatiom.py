import geocoder
import folium

g = geocoder.ip('me')
print(g.latlng)
my_map1 = folium.Map(location = [41.2619, -95.8608], zoom_start = 12)
folium.Marker([41.2619, -95.8608], popup = 'Current Location').add_to(my_map1)
print(my_map1)

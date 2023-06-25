"""
This code generates all possible routes using the API from point to point.
"""

from datetime import datetime, timedelta
import googlemaps
import folium
import polyline

#Carbon Emissions
    # MRT - 13g of CO2 per km source: https://www.lta.gov.sg/content/ltagov/en/who_we_are/statistics_and_publications/Connect/greenmrtstations.html
    # Bus - 105g of CO2 per km source:  https://ourworldindata.org/travel-carbon-footprint
    # Motorcycle - 103g per km source: https://ourworldindata.org/travel-carbon-footprint
    # Cars (medium petrol) - 192g per km source: https://ourworldindata.org/travel-carbon-footprint
    # Cars (medium Diesel) - 171g per km source: https://ourworldindata.org/travel-carbon-footprint
# Carbon Emission Constants (in grams of CO2 per km)
SUBWAY_EMISSION = 13
BUS_EMISSION = 105
DRIVING_EMISSION = 182
WALKING_EMISSION = 0.0

gmaps = googlemaps.Client(key='AIzaSyAKahoi1o9xL4-dwGJE_5GuQI0uAucQ8Vk')

def get_formatted_address(lat, lng):
    result = gmaps.reverse_geocode((lat, lng))
    if result:
        return result[0]['formatted_address']
    return ""

def print_step_details(step, distance):
    start_location = step['start_location']
    end_location = step['end_location']
    start_address = get_formatted_address(start_location['lat'], start_location['lng'])
    end_address = get_formatted_address(end_location['lat'], end_location['lng'])
    travel_mode = step['travel_mode']

    if travel_mode == 'TRANSIT':

        transit_details = step['transit_details']
        line = transit_details['line']
        vehicle = line['vehicle']
        vehicle_type = vehicle['type']
        print(f"Take {vehicle_type} ({line['name']}) from {start_address} to {end_address}")

        if vehicle_type == 'SUBWAY':
            emissions = SUBWAY_EMISSION * distance
        else:
            emissions = BUS_EMISSION * distance

    elif travel_mode == 'WALKING':
        print(f"Walk from {start_address} to {end_address}")
        emissions = WALKING_EMISSION * distance

    else:
        print(f"{travel_mode} from {start_address} to {end_address}")
        emissions = DRIVING_EMISSION * distance

    print(f"Distance: {distance:.2f} km")
    print(f"Carbon Emissions: {emissions:.2f} g CO2\n")
    return emissions

def calculate_total_distance(results):
    total_distance = sum(leg['distance']['value'] for leg in results[0]['legs'])
    return total_distance / 1000  # Convert distance to kilometers

def calculate_total_duration(results):
    total_duration = sum(leg['duration']['value'] for leg in results[0]['legs'])
    return total_duration / 60  # Convert duration to minutes

origin = input("Please enter a valid starting address: ")
destination = input("Please enter a valid destination address: ")

transit_mode = input("Choose travel mode (options: driving, transit, walking): ")

# Get directions from Google Maps API
results = gmaps.directions(origin, destination, mode=transit_mode, arrival_time=datetime.now() + timedelta(minutes=0.5))
print('\nDirections:')

total_emissions = 0.0

# Get directions from Google Maps API with alternatives
results = gmaps.directions(origin, destination, mode=transit_mode, arrival_time=datetime.now() + timedelta(minutes=0.5), alternatives=True)

route_count=0
# Print the steps for each route
for route in results:
    print('\nRoute:',route_count)
    total_emissions = 0.0
    route_count+=1

    for leg in route['legs']:

        for step in leg['steps']:

            distance = step['distance']['value'] / 1000  # Convert distance to kilometers
            emissions = print_step_details(step, distance)
            total_emissions += emissions

    print(f"Total Carbon Emissions: {total_emissions:.2f} g CO2")

    total_distance = calculate_total_distance(results)
    print(f"Total distance: {total_distance} kilometers")

    total_duration = calculate_total_duration(results)
    print(f"Total duration: {total_duration:.2f} minutes\n")


# Extract the destination latitude and longitude
destination_lat = results[0]['legs'][-1]['end_location']['lat']
destination_lng = results[0]['legs'][-1]['end_location']['lng']

# Create a map centered on the origin location
origin_lat = results[0]['legs'][0]['start_location']['lat']
origin_lng = results[0]['legs'][0]['start_location']['lng']
map_center = [origin_lat, origin_lng]
map_zoom = 12

# Create a map
map = folium.Map(location=map_center, zoom_start=map_zoom)

# Add markers for the origin and destination
origin_address = results[0]['legs'][0]['start_address']
destination_address = results[0]['legs'][-1]['end_address']
folium.Marker(location=[origin_lat, origin_lng], popup=origin_address, icon=folium.Icon(color='blue')).add_to(map)
folium.Marker(location=[destination_lat, destination_lng], popup=destination_address, icon=folium.Icon(color='red')).add_to(map)

# Add polylines for each step of the journey
for leg in results[0]['legs']:

    for step in leg['steps']:

        polyline_points = step['polyline']['points']
        polyline_locations = polyline.decode(polyline_points)
        folium.PolyLine(locations=polyline_locations, color='green', weight=2).add_to(map)

# Display the map
map_name = input("\nSave your map by entering a name (if not, leave it blank): ")

if map_name:
    map.save(map_name + ".html")



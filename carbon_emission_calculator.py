import googlemaps
import heapq
from bs4 import BeautifulSoup
import folium
import polyline

from datetime import datetime, timedelta

# Carbon Emissions MRT - 13g of CO2 per km source:
# https://www.lta.gov.sg/content/ltagov/en/who_we_are/statistics_and_publications/Connect/greenmrtstations.html Bus -
# 105g of CO2 per km source:  https://ourworldindata.org/travel-carbon-footprint Motorcycle - 103g per km source:
# https://ourworldindata.org/travel-carbon-footprint Cars (medium petrol) - 192g per km source:
# https://ourworldindata.org/travel-carbon-footprint Cars (medium Diesel) - 171g per km source:
# https://ourworldindata.org/travel-carbon-footprint

# Carbon Emission Constants (in grams of CO2 per km)
SUBWAY_EMISSION = 13
BUS_EMISSION = 105
DRIVING_EMISSION = 182
CAR_PET_EMISSION = 192
CAR_DES_EMISSION = 171
MTRCYCLE_EMISSION = 103
WALKING_EMISSION = 0.0


def calculate_total_distance(route):
    return sum(leg['distance']['value'] for leg in route['legs']) / 1000  # Convert to km


def calculate_total_duration(route):
    return sum(leg['duration']['value'] for leg in route['legs']) / 60  # Convert to minutes


# def calculate_total_emissions(route):
#     total_emissions = 0.0
#     for leg in route['legs']:
#         for step in leg['steps']:
#             distance = step['distance']['value'] / 1000  # Convert to km
#             if step['travel_mode'] == 'TRANSIT':
#                 vehicle_type = step['transit_details']['line']['vehicle']['type']
#                 emissions = SUBWAY_EMISSION * distance if vehicle_type == 'SUBWAY' else BUS_EMISSION * distance
#             elif step['travel_mode'] == 'WALKING':
#                 emissions = WALKING_EMISSION * distance
#             else:
#                 emissions = DRIVING_EMISSION * distance
#             total_emissions += emissions
#     return total_emissions

def calculate_total_emissions(route, vehicle_type=None, fuel_type=None):
    total_emissions = 0.0
    for leg in route['legs']:
        for step in leg['steps']:
            distance = step['distance']['value'] / 1000  # Convert to km
            if step['travel_mode'] == 'TRANSIT':
                vehicle_type = step['transit_details']['line']['vehicle']['type']
                emissions = SUBWAY_EMISSION * distance if vehicle_type == 'SUBWAY' else BUS_EMISSION * distance
            elif step['travel_mode'] == 'WALKING':
                emissions = WALKING_EMISSION * distance
            else:
                if vehicle_type == 'car':
                    if fuel_type == 'petrol':
                        emissions = CAR_PET_EMISSION * distance
                    elif fuel_type == 'diesel':
                        emissions = CAR_DES_EMISSION * distance
                elif vehicle_type == 'motorcycle':
                    emissions = MTRCYCLE_EMISSION * distance
                else:
                    emissions = 0.0  # Default value if vehicle type is invalid
            total_emissions += emissions
    return total_emissions

def print_route_details(route):
    for i, leg in enumerate(route['legs']):
        print(f"\nLeg {i + 1}:")
        for j, step in enumerate(leg['steps']):
            if step['travel_mode'] == 'TRANSIT':
                transit_details = step['transit_details']
                instructions = remove_html_tags(step['html_instructions'])
                print(
                    f"  Step {j + 1}: {instructions} (Distance: {step['distance']['text']}, Duration: {step['duration']['text']})")
                print(f"    Depart from: {transit_details['departure_stop']['name']}")
                print(f"    Arrive at: {transit_details['arrival_stop']['name']}")
                print(f"    Vehicle: {transit_details['line']['vehicle']['name']}")
                print(f"    Line: {transit_details['line']['name']}")
            else:
                instructions = remove_html_tags(step['html_instructions'])
                print(
                    f"  Step {j + 1}: {instructions} (Distance: {step['distance']['text']}, Duration: {step['duration']['text']})")


def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text(separator=' ')


# Connect to Google Maps API
gmaps = googlemaps.Client(key='AIzaSyAKahoi1o9xL4-dwGJE_5GuQI0uAucQ8Vk')

# Get user input
origin = input("Please enter a valid starting address: ")
destination = input("Please enter a valid destination address: ")
transit_mode = input("Choose travel mode (options: driving, transit, walking): ")

# Define default values for vehicle_type and fuel_type
vehicle_type = None
fuel_type = None

if transit_mode == 'driving':
    vehicle_type = input("Choose vehicle type (options: car, motorcycle): ")
    if vehicle_type == 'car':
        fuel_type = input("Choose fuel type (options: petrol, diesel): ")

# Get directions from Google Maps API
results = gmaps.directions(origin, destination, mode=transit_mode, alternatives=True)

# Create heaps for each metric
distance_heap = []
duration_heap = []
emissions_heap = []

# Populate heaps with (metric, route_id) tuples
for i, route in enumerate(results):
    total_distance = calculate_total_distance(route)
    total_duration = calculate_total_duration(route)
    total_emissions = calculate_total_emissions(route, vehicle_type, fuel_type)
    heapq.heappush(distance_heap, (total_distance, i))
    heapq.heappush(duration_heap, (total_duration, i))
    heapq.heappush(emissions_heap, (total_emissions, i))

# Get user input for sorting metric
metric = input("Choose a sorting metric (options: distance, duration, emissions): ")

# Display best route based on chosen metric
print("\nBest route by " + metric + ":")
if metric == 'distance':
    total_distance, route_id = heapq.heappop(distance_heap)
    print(f"\nRoute ID: {route_id}, Total distance: {total_distance} km")
    print_route_details(results[route_id])
elif metric == 'duration':
    total_duration, route_id = heapq.heappop(duration_heap)
    print(f"\nRoute ID: {route_id}, Total duration: {total_duration} min")
    print_route_details(results[route_id])
elif metric == 'emissions':
    total_emissions, route_id = heapq.heappop(emissions_heap)
    print(f"\nRoute ID: {route_id}, Total carbon emissions: {total_emissions} g CO2")
    print_route_details(results[route_id])

# Extract the destination latitude and longitude
destination_lat = results[route_id]['legs'][-1]['end_location']['lat']
destination_lng = results[route_id]['legs'][-1]['end_location']['lng']

# Create a map centered on the origin location
origin_lat = results[route_id]['legs'][0]['start_location']['lat']
origin_lng = results[route_id]['legs'][0]['start_location']['lng']
map_center = [origin_lat, origin_lng]
map_zoom = 12

# Create a map
map = folium.Map(location=map_center, zoom_start=map_zoom)

# Add markers for the origin and destination
origin_address = results[route_id]['legs'][0]['start_address']
destination_address = results[route_id]['legs'][-1]['end_address']
folium.Marker(location=[origin_lat, origin_lng], popup=origin_address, icon=folium.Icon(color='blue')).add_to(map)
folium.Marker(location=[destination_lat, destination_lng], popup=destination_address,
              icon=folium.Icon(color='red')).add_to(map)

# Add polylines for each step of the journey
for leg in results[route_id]['legs']:
    for step in leg['steps']:
        polyline_points = step['polyline']['points']
        polyline_locations = polyline.decode(polyline_points)
        folium.PolyLine(locations=polyline_locations, color='green', weight=2).add_to(map)

# Display the map
map_name = input("\nSave your map by entering a name (if not, leave it blank): ")
if map_name:
    map.save(map_name + ".html")

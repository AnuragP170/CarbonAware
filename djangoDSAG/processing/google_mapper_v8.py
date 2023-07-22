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

import sys

try:
    transportMode=(sys.argv[1])
    vehicleType=(sys.argv[2])
    fuelType=(sys.argv[3])
    startPoint = (sys.argv[4])
    endPoint = (sys.argv[5])
    metricType = (sys.argv[6])
except:
    print("Your input is invalid!")

def calculate_total_distance(route):
    return sum(leg['distance']['value'] for leg in route['legs']) / 1000  # Convert to km


def calculate_total_duration(route):
    return sum(leg['duration']['value'] for leg in route['legs']) / 60  # Convert to minutes

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
            elif step['travel_mode'] == "DRIVING":
                if vehicle_type == 'car':
                    if fuel_type == 'petrol':
                        emissions = CAR_PET_EMISSION * distance
                    elif fuel_type == 'diesel':
                        emissions = CAR_DES_EMISSION * distance
                elif vehicle_type == 'motorcycle':
                    emissions = MTRCYCLE_EMISSION * distance
                else:
                    emissions = 0.0  # Default value if vehicle type is invalid
            else:
                print("An error occurred, please contact us at (put email here).")
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
origin = startPoint
destination = endPoint
transit_mode = transportMode.lower()

# Define default values for vehicle_type and fuel_type
vehicle_type = None
fuel_type = None

if transit_mode == 'driving':
    vehicle_type = vehicleType.lower()
    if vehicle_type == 'car':
        fuel_type = fuelType.lower()

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
metric = metricType.lower()

# Display best route based on chosen metric
print("\nBest route by " + metric + ":")
if metric == 'distance':
    total_distance, route_id = heapq.heappop(distance_heap)
    print(f"\nRoute ID: {route_id}, Total distance: {total_distance:.2f} km")
    print_route_details(results[route_id])
elif metric == 'duration':
    total_duration, route_id = heapq.heappop(duration_heap)
    print(f"\nRoute ID: {route_id}, Total duration: {total_duration:.2f} min")
    print_route_details(results[route_id])
elif metric == 'emissions':
    total_emissions, route_id = heapq.heappop(emissions_heap)
    print(f"\nRoute ID: {route_id}, Total carbon emissions: {total_emissions:.2f} g CO2")
    print_route_details(results[route_id])
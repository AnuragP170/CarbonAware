from datetime import datetime, timedelta
import googlemaps
import folium
import polyline

# failed attempt to create a linkedlist data structure to store directions.

class Node:
    def __init__(self, source, destination, carbon_emission, distance):
        self.source = source
        self.destination = destination
        self.carbon_emission = carbon_emission
        self.distance = distance
        self.next = None

# Carbon Emissions Constants (in grams of CO2 per km)
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

total_emissions = 0.0

origin = input("Please enter a valid starting address: ")
destination = input("Please enter a valid destination address: ")

transit_mode = input("Choose travel mode (options: driving, transit, walking): ")

# Get directions from Google Maps API
results = gmaps.directions(origin, destination, mode=transit_mode, arrival_time=datetime.now() + timedelta(minutes=0.5))
print('\nDirections:')

# Create the head node of the linked list
head = None
current = None

# Print the steps for each leg of the journey
for leg in results[0]['legs']:
    print(f"Start address: {get_formatted_address(leg['start_location']['lat'], leg['start_location']['lng'])}")
    print(f"End address: {get_formatted_address(leg['end_location']['lat'], leg['end_location']['lng'])}\n")

    for step in leg['steps']:
        distance = step['distance']['value'] / 1000  # Convert distance to kilometers
        emissions = print_step_details(step, distance)
        total_emissions += emissions
        source_address = step['start_address']
        destination_address = step['end_address']

        # Create a new node
        node = Node(source_address, destination_address, emissions, distance)

        if head is None:
            # If it's the first node, set it as the head
            head = node
            current = head
        else:
            # Link the current node to the new node
            current.next = node
            current = current.next

total_distance = calculate_total_distance(results)
total_duration = calculate_total_duration(results)

# Traverse the linked list and display the details
current = head
while current is not None:
    print(f"Source: {current.source}")
    print(f"Destination: {current.destination}")
    print(f"Carbon Emissions: {current.carbon_emission:.2f} g CO2")
    print(f"Distance: {current.distance:.2f} km\n")
    current = current.next

print(f"Total Carbon Emissions: {total_emissions:.2f} g CO2")
print(f"Total Distance: {total_distance:.2f} kilometers")
print(f"Total Duration: {total_duration:.2f} minutes")

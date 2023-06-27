# Includes a function that uses Google Maps API to calculate distance between MRT stations (nodes)
# Generates a list (collection of tuples) of format [(start, end, distance)]
# needs to be imported into main code to generate the list. eg: (import node_distance_calculator as nodeDist)

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAKahoi1o9xL4-dwGJE_5GuQI0uAucQ8Vk')

def mrt_list_generator(mrt_array):
    distances = []
    for i in range(len(mrt_array) - 1):
        start = mrt_array[i] + ' MRT Station, Singapore'
        end = mrt_array[i + 1] + ' MRT Station, Singapore'
        directions_result = gmaps.directions(start, end)

        if directions_result:
            # Extract the distance from the directions result
            distance = directions_result[0]['legs'][0]['distance']['text']
            start = start.replace(' MRT Station, Singapore', '')
            end = end.replace(' MRT Station, Singapore', '')
            distance = distance.replace(' km', '')
            distance = float(distance)
            distances.append((start, end, distance))
        else:
            start = start.replace(' MRT Station, Singapore', '')
            end = end.replace(' MRT Station, Singapore', '')
            distance = distance.replace(' km', '')
            distance = float(distance)
            distances.append((start, end, "No directions found."))

    return distances


# # Print the stored distances
# for start, end, distance in distances:
#     print(f"The distance from {start} to {end} is {distance}.")



"""
# Code to save data into an Excel file.

import googlemaps
import pandas as pd
# install openpyxl

gmaps = googlemaps.Client(key='AIzaSyAKahoi1o9xL4-dwGJE_5GuQI0uAucQ8Vk')
mrt_array = ['HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa', 'Kent Ridge', 'one-north', 'Buona Vista', 'Holland Village', 'Farrer Road', 'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon', 'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten', 'Stadium', 'Nicoll Highway', 'Promenade']

data = []

input_mrt = yellow_1
for i in range(len(input_mrt) - 1):
    start = input_mrt[i] + ' MRT Station, Singapore'
    end = input_mrt[i + 1] + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)

    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    # Remove 'MRT Station, Singapore' from start and end strings
    start = start.replace(' MRT Station, Singapore', '')
    end = end.replace(' MRT Station, Singapore', '')

    data.append([start, end, distance])

# Create a DataFrame from the data list
df = pd.DataFrame(data, columns=["Start", "End", "Distance"])

# Save the DataFrame to an Excel file
df.to_excel("distances1.xlsx", index=False) """

"""
# Original Code

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAKahoi1o9xL4-dwGJE_5GuQI0uAucQ8Vk')

yellow_1 = ['HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa', 'Kent Ridge', 'one-north', 'Buona Vista', 'Holland Village', 'Farrer Road', 'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon', 'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten', 'Stadium', 'Nicoll Highway', 'Promenade']

for i in range(len(yellow_1) - 1):
    start = yellow_1[i] + ' MRT Station, Singapore'
    end = yellow_1[i + 1] + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)

    if directions_result:
        # Extract the distance from the directions result
        distance = directions_result[0]['legs'][0]['distance']['text']
        print(f"The distance from {start} to {end} is {distance}.")
    else:
        print(f"No directions found for {start} to {end}.")


"""

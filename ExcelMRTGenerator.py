import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyAKahoi1o9xL4-dwGJE_5GuQI0uAucQ8Vk')

yellow_stations = ['HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa',
                   'Kent Ridge', 'One-north', 'Buona Vista', 'Holland Village', 'Farrer Road',
                   'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon',
                   'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten',
                   'Stadium', 'Nicoll Highway', 'Promenade']

yellow_1 = ['Promenade', 'Bayfront', 'Marina Bay']
yellow_2 = ['Promenade', 'Esplanade', 'Bras Basah', 'Dhoby Ghaut']

red_stations = ['Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji', 'Marsiling',
                'Woodlands', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang', 'Ang Mo Kio',
                'Bishan', 'Braddell', 'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset', 'Dhoby Ghaut',
                'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South Pier']

purple_stations = ['HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India',
                   'Farrer Park', 'Boon Keng', 'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang',
                   'Buangkok', 'Sengkang', 'Punggol']
green_stations = ['Tuas Link', 'Tuas West Road', 'Tuas Crescent', 'Gul Circle', 'Joo Koon', 'Pioneer', 'Boon Lay',
                  'Lakeside', 'Chinese Garden', 'Jurong East', 'Clementi', 'Dover', 'Buona Vista', 'Commonwealth',
                  'Queenstown', 'Redhill', 'Tiong Bahru', 'Outram Park', 'Tanjong Pagar', 'Raffles Place', 'City Hall',
                  'Bugis', 'Lavender', 'Kallang', 'Aljunied', 'Paya Lebar', 'Eunos', 'Kembangan', 'Bedok',
                  'Tanah Merah']

green_1 = ['Tanah Merah','Simei', 'Tampines', 'Pasir Ris']
green_2 = ['Tanah Merah','Expo', 'Changi Airport']

blue_stations = ["Bukit Panjang", "Cashew", "Hillview", "Beauty World", "King Albert Park", "Sixth Avenue",
                 "Tan Kah Kee", "Botanic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis",
                 "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen",
                 "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit",
                 "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi",
                 "Expo"]

brown_stations = ["Woodlands North", "Woodlands", "Woodlands South", "Springleaf", "Lentor", "Mayflower",
                  "Bright Hill", "Upper Thomson", "Caldecott", "Stevens", "Napier", "Orchard Boulevard",
                  "Orchard", "Great World", "Havelock", "Outram Park", "Maxwell", "Shenton Way", "Marina Bay",
                  "Gardens by the Bay"]


# yellow dataframe
yellow_data = []

# yellow stations
for station in yellow_stations:
    if station in yellow_1 or station in yellow_2:
        continue

    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = yellow_stations[yellow_stations.index(station) + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    yellow_data.append([station, start_lat, start_lng, distance, next_station])

# adjustments to yellow line
# yellow 1 - Promenade to Bayfront to Marina Bay
for i in range(len(yellow_1) - 1):
    station = yellow_1[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = yellow_1[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    yellow_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in yellow_1
last_station_yellow_1 = yellow_1[-1]
start = last_station_yellow_1 + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
yellow_data.append([last_station_yellow_1, start_lat, start_lng, "N/A", "N/A"])

# yellow 2 - Promenade to Esplanade to Bras Basah to Dhoby Ghaut
for i in range(len(yellow_2) - 1):
    station = yellow_2[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = yellow_2[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    yellow_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in yellow_2
last_station_yellow_2 = yellow_2[-1]
start = last_station_yellow_2 + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
yellow_data.append([last_station_yellow_2, start_lat, start_lng, "N/A", "N/A"])


# red dataframe
red_data = []

# red stations
for i in range(len(red_stations) - 1):
    station = red_stations[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = red_stations[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    red_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in red
last_station_red = red_stations[-1]
start = last_station_red + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
red_data.append([last_station_red, start_lat, start_lng, "N/A", "N/A"])

# purple dataframe
purple_data = []

# purple stations
for i in range(len(purple_stations) - 1):
    station = purple_stations[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = purple_stations[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    purple_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in purple
last_station_purple = purple_stations[-1]
start = last_station_purple + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
purple_data.append([last_station_purple, start_lat, start_lng, "N/A", "N/A"])

# green dataframe
green_data = []

# green stations
for station in green_stations:
    if station in green_1 or station in green_2:
        continue

    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = green_stations[green_stations.index(station) + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    green_data.append([station, start_lat, start_lng, distance, next_station])

# adjustments to green line
# green 1
for i in range(len(green_1) - 1):
    station = green_1[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = green_1[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    green_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in green_1
last_station_green_1 = green_1[-1]
start = last_station_green_1 + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
green_data.append([last_station_green_1, start_lat, start_lng, "N/A", "N/A"])

# green 2
for i in range(len(green_2) - 1):
    station = green_2[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = green_2[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    green_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in green_2
last_station_green_2 = green_2[-1]
start = last_station_green_2 + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
green_data.append([last_station_green_2, start_lat, start_lng, "N/A", "N/A"])


# blue dataframe
blue_data = []

# blue stations
for i in range(len(blue_stations) - 1):
    station = blue_stations[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = blue_stations[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    blue_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in blue
last_station_blue = blue_stations[-1]
start = last_station_blue + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
blue_data.append([last_station_blue, start_lat, start_lng, "N/A", "N/A"])

# brown dataframe
brown_data = []

# brown stations
for i in range(len(brown_stations) - 1):
    station = brown_stations[i]
    start = station + ' MRT Station, Singapore'
    start_geocode = gmaps.geocode(start)
    start_lat = start_geocode[0]["geometry"]["location"]["lat"]
    start_lng = start_geocode[0]["geometry"]["location"]["lng"]

    next_station = brown_stations[i + 1]
    end = next_station + ' MRT Station, Singapore'
    directions_result = gmaps.directions(start, end)
    if directions_result:
        distance = directions_result[0]['legs'][0]['distance']['text']
    else:
        distance = "N/A"

    brown_data.append([station, start_lat, start_lng, distance, next_station])

# modify the last station in brown
last_station_brown = brown_stations[-1]
start = last_station_brown + ' MRT Station, Singapore'
start_geocode = gmaps.geocode(start)
start_lat = start_geocode[0]["geometry"]["location"]["lat"]
start_lng = start_geocode[0]["geometry"]["location"]["lng"]
brown_data.append([last_station_brown, start_lat, start_lng, "N/A", "N/A"])

# create dataframes for each line
df_yellow = pd.DataFrame(yellow_data, columns=["Station", "Latitude", "Longitude", "Distance", "Next Station"])
df_red = pd.DataFrame(red_data, columns=["Station", "Latitude", "Longitude", "Distance", "Next Station"])
df_purple = pd.DataFrame(purple_data, columns=["Station", "Latitude", "Longitude", "Distance", "Next Station"])
df_green = pd.DataFrame(green_data, columns=["Station", "Latitude", "Longitude", "Distance", "Next Station"])
df_blue = pd.DataFrame(blue_data, columns=["Station", "Latitude", "Longitude", "Distance", "Next Station"])
df_brown = pd.DataFrame(brown_data, columns=["Station", "Latitude", "Longitude", "Distance", "Next Station"])

# save dataframes to separate tabs in excel file
with pd.ExcelWriter('distances.xlsx') as writer:
    df_yellow.to_excel(writer, sheet_name='Yellow_Line', index=False)
    df_red.to_excel(writer, sheet_name='Red_Line', index=False)
    df_purple.to_excel(writer, sheet_name='Purple_Line', index=False)
    df_green.to_excel(writer, sheet_name='Green_Line', index=False)
    df_blue.to_excel(writer, sheet_name='Blue_Line', index=False)
    df_brown.to_excel(writer, sheet_name='Brown_Line', index=False)

print("excel generated with no issue")

import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyAKahoi1o9xL4-dwGJE_5GuQI0uAucQ8Vk')

yellow_1 = ['HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa', 'Kent Ridge', 'one-north', 'Buona Vista', 'Holland Village', 'Farrer Road', 'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon', 'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten', 'Stadium', 'Nicoll Highway', 'Promenade']
red_stations = ['Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji', 'Marsiling', 'Woodlands', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang', 'Ang Mo Kio', 'Bishan', 'Braddell', 'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset', 'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South Pier']
stations = [yellow_1, red_stations]
sheet_names = ["Yellow_Line", "Red_Line"]

with pd.ExcelWriter('distances.xlsx') as writer:
    for i, line in enumerate(stations):
        data = []
        for j in range(len(line) - 1):
            start = line[j] + ' MRT Station, Singapore'
            end = line[j + 1] + ' MRT Station, Singapore'
            directions_result = gmaps.directions(start, end)
            if directions_result:
                distance = directions_result[0]['legs'][0]['distance']['text']
            else:
                distance = "N/A"

            # Getting the latitude and longitude of the start and end
            start_geocode = gmaps.geocode(start)
            start_lat = start_geocode[0]["geometry"]["location"]["lat"]
            start_lng = start_geocode[0]["geometry"]["location"]["lng"]

            end_geocode = gmaps.geocode(end)
            end_lat = end_geocode[0]["geometry"]["location"]["lat"]
            end_lng = end_geocode[0]["geometry"]["location"]["lng"]

            data.append([start, start_lat, start_lng, end, end_lat, end_lng, distance])

        # Create a DataFrame from the data list
        df = pd.DataFrame(data, columns=["Start", "Start_Lat", "Start_Lng", "End", "End_Lat", "End_Lng", "Distance"])

        # Save the DataFrame to an Excel file
        df.to_excel(writer, sheet_name=sheet_names[i], index=False)




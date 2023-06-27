import folium
import pandas as pd

# Create a map centered at an arbitrary location
m = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB Positron', zoom_start=12)

with pd.ExcelFile('distances.xlsx') as xls:
    for sheet_name, color in zip(xls.sheet_names, ["orange", "red"]):
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Add a line for every record in the filtered data
        for i in range(0, len(df)):
            start_coords = [df.iloc[i]['Start_Lat'], df.iloc[i]['Start_Lng']]
            end_coords = [df.iloc[i]['End_Lat'], df.iloc[i]['End_Lng']]

            # Connect start and end locations with a line
            folium.PolyLine(locations=[start_coords, end_coords], color=color).add_to(m)

# Save the map to an html
m.save('mrt_stations.html')
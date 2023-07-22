import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
from . import concatDir as dirJoin
import mpld3

def generateMRTimage(startMRT, endMRT):

    pwd = os.getcwd()
    directory = dirJoin.concatDir(pwd, "/processing")
    excelFile = directory + "/" + "distances.xlsx"

    # read the excel files for each line
    df_yellow = pd.read_excel(excelFile, sheet_name='Yellow_Line')
    df_red = pd.read_excel(excelFile, sheet_name='Red_Line')
    df_purple = pd.read_excel(excelFile, sheet_name='Purple_Line')
    df_green = pd.read_excel(excelFile, sheet_name='Green_Line')
    df_blue = pd.read_excel(excelFile, sheet_name='Blue_Line')
    df_brown = pd.read_excel(excelFile, sheet_name='Brown_Line')

    # create an empty graph
    G = nx.Graph()

    # function to add nodes and edges to graph
    def add_nodes_edges(data, color, node_size, edge_color, line_name):
        for _, row in data.iterrows():
            start = row['Station']
            start_lat = row['Latitude']
            start_lng = row['Longitude']
            distance = row['Distance']
            end = row['Next Station']

            # add nodes with specified color and node size
            node_name = f'{start} ({line_name})'
            G.add_node(node_name, Latitude=start_lat, Longitude=start_lng, color=color, size=node_size)

            # add edges to the graph
            # exclude last stations
            if pd.notna(end):
                # Remove 'km' and convert to float
                distance = float(distance.replace(' km', ''))

                # Add edges
                edge_name = f'{start} ({line_name}) - {end} ({line_name})'
                G.add_edge(node_name, f'{end} ({line_name})', weight=distance, color=edge_color, name=edge_name)


    def connect_shared_stations(interchange_stations):
        for station in interchange_stations:
            shared_nodes = [node for node in G.nodes if station in node]
            for i in range(len(shared_nodes) - 1):
                for j in range(i + 1, len(shared_nodes)):
                    G.add_edge(shared_nodes[i], shared_nodes[j], weight=0)

    def find_interchange_stations(dfs):
        # create a dictionary to count appearances of stations
        station_counts = dict()

        # iterate over dataframes and count appearances of each station
        for df in dfs:
            for station in df['Station']:
                station_counts[station] = station_counts.get(station, 0) + 1

        # filter out stations that appear in more than one dataframe (interchange stations)
        interchange_stations = [station for station, count in station_counts.items() if count > 1]

        return interchange_stations

    # get the list of interchange stations
    interchange_stations = find_interchange_stations([df_yellow, df_red, df_purple, df_green, df_blue, df_brown])

    # add nodes and edges for each line with respective colors and node sizes
    add_nodes_edges(df_yellow, color='orange', node_size=200, edge_color='orange', line_name='Yellow Line')
    add_nodes_edges(df_red, color='red', node_size=180, edge_color='red', line_name='Red Line')
    add_nodes_edges(df_purple, color='purple', node_size=100, edge_color='purple', line_name='Purple Line')
    add_nodes_edges(df_green, color='green', node_size=90, edge_color='green', line_name='Green Line')
    add_nodes_edges(df_blue, color='blue', node_size=80, edge_color='blue', line_name='Blue Line')
    add_nodes_edges(df_brown, color='brown', node_size=90, edge_color='brown', line_name='Brown Line')

    # connect shared stations
    connect_shared_stations(interchange_stations)

    # adding/removing missing or extra edges
    G['Tampines West (Blue Line)']['Tampines (Blue Line)']['weight'] = 1.6
    G['Tampines (Blue Line)']['Tampines East (Blue Line)']['weight'] = 2.0
    G['Orchard Boulevard (Brown Line)']['Orchard (Brown Line)']['weight'] = 1.7
    G['Woodlands North (Brown Line)']['Woodlands (Brown Line)']['weight'] = 3.4
    G['Woodlands (Brown Line)']['Woodlands South (Brown Line)']['weight'] = 1.9
    # Remove some edges
    G.remove_edge('Tampines West (Blue Line)', 'Tampines East (Blue Line)')
    G.remove_edge('Woodlands North (Brown Line)', 'Woodlands South (Brown Line)')

    # create positions dictionary with node coordinates
    scale_factor = 5
    positions = {}
    for node in G.nodes:
        positions[node] = (G.nodes[node]['Longitude']*scale_factor, G.nodes[node]['Latitude']*scale_factor)

    # plot the graph
    fig = plt.figure(figsize=(13, 11))

    # add labels to nodes
    labels = {node: node.split('(')[0] for node in G.nodes}

    # iterate over nodes and set color and size attributes
    for node, data in G.nodes(data=True):
        color = data.get('color', 'gray') # use gray as default color if no color is specified
        size = data.get('size', 100) # use 100 as default size if no size is specified
        nx.draw_networkx_nodes(G, positions, nodelist=[node], node_color=color, node_size=size)

    # iterate over edges and set edge color
    for u, v, data in G.edges(data=True):
        color = data.get('color', 'gray') # use gray as default color if no color is specified
        nx.draw_networkx_edges(G, positions, edgelist=[(u, v)], edge_color=color)


    # print all edges for debugging

    # # Iterate over edges in the graph and print them
    # for u, v, data in G.edges(data=True):
    #     print(f"Edge: {u} -- {v} with weight: {data['weight']}")

    # Define start and end nodes
    start_node = startMRT
    end_node = endMRT

    # Use Dijkstra's algorithm to find the shortest path
    shortest_path = nx.dijkstra_path(G, start_node, end_node, weight='weight')

    # Get the list of edges in the shortest path
    shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path) - 1)]

    # draw the shortest path in pink
    nx.draw_networkx_edges(G, positions, edgelist=shortest_path_edges, edge_color='magenta', width=5)

    nx.draw_networkx_labels(G, positions, labels, font_size=5)

    # Print shortest path
    print(' -> '.join(shortest_path))
    # Compute the length of the shortest path
    shortest_path_length = nx.dijkstra_path_length(G, start_node, end_node, weight='weight')
    print(f"The total distance of the shortest path is: {round(shortest_path_length, 2)} km")
    print(f"The est. carbon emission is: {round(shortest_path_length*13)} g")
    # display the graph
    plt.axis('off')

    graph = mpld3.fig_to_html(fig)

    return graph

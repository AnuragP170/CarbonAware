# import networkx as nx
# import node_distance_calculator as nodeDist
#
# class Graph:
#     def __init__(self):
#         self.nodes = {}
#
#     def add_node(self, node):
#         self.nodes[node] = {}
#
#     def add_edge(self, node1, node2, weight):
#         self.nodes[node1][node2] = weight
#         self.nodes[node2][node1] = weight
#
#     def dijkstra(self, start_node, end_node):
#         distances = {node: float('inf') for node in self.nodes}
#         distances[start_node] = 0
#         visited = set()
#
#         while len(visited) < len(self.nodes):
#             current_node = None
#             min_distance = float('inf')
#
#             for node in self.nodes:
#                 if node not in visited and distances[node] < min_distance:
#                     current_node = node
#                     min_distance = distances[node]
#
#             if current_node is None:  # Exit the loop if no valid node is found
#                 break
#
#             visited.add(current_node)
#
#             if current_node == end_node:  # Exit the loop if the end node is reached
#                 break
#
#             for neighbor, weight in self.nodes[current_node].items():
#                 distance = distances[current_node] + weight
#                 if distance < distances[neighbor]:
#                     distances[neighbor] = distance
#
#         return distances[end_node]
# def add_stations_to_graph(graph, G, line_info, stations, line_name):
#     for edge in stations:
#         G.add_edge(edge[0], edge[1], weight=edge[2])
#         graph.add_node(edge[0])  # Add the source node
#         graph.add_node(edge[1])  # Add the destination node
#         graph.add_edge(edge[0], edge[1], edge[2])
#         line_info[(edge[0], edge[1])] = line_name  # Store line information
#         line_info[(edge[1], edge[0])] = line_name  # Store line information for the reverse edge
#
#
# # List of all stations (red, yellow, etc.)
#
# red_stations = ['Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji',
#                 'Marsiling', 'Woodlands', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang',
#                 'Ang Mo Kio', 'Bishan', 'Braddell', 'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset',
#                 'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South Pier']
#
# yellow_stations = ['HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa', 'Kent Ridge', 'one-north', 'Buona Vista', 'Holland Village', 'Farrer Road', 'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon', 'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten', 'Stadium', 'Nicoll Highway', 'Promenade']
# yellow_1 = ['Promenade', 'Bayfront', 'Marina Bay']
# yellow_2 = ['Promenade', 'Esplanade', 'Bras Basah', 'Dhoby Ghaut']
# purple_stations = ['HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng', 'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang', 'Punggol']
# green_stations = ['Tuas Link', 'Tuas West Road', 'Tuas Crescent', 'Gul Circle', 'Joo Koon', 'Pioneer', 'Boon Lay', 'Lakeside', 'Chinese Garden', 'Jurong East', 'Clementi', 'Dover', 'Buona Vista', 'Commonwealth', 'Queenstown', 'Redhill', 'Tiong Bahru', 'Outram Park', 'Tanjong Pagar', 'Raffles Place', 'City Hall', 'Bugis', 'Lavender', 'Kallang', 'Aljunied', 'Paya Lebar', 'Eunos', 'Kembangan', 'Bedok', 'Tanah Merah']
# green_main = ['Tanah Merah','Simei', 'Tampines', 'Pasir Ris']
# green_extended = ['Tanah Merah','Expo', 'Changi Airport']
# blue_stations = ["Bukit Panjang", "Cashew", "Hillview", "Beauty World", "King Albert Park", "Sixth Avenue", "Tan Kah Kee", "Botanic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis", "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen", "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit", "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi", "Expo"]
# brown_stations = ["Woodlands North", "Woodlands", "Woodlands South", "Springleaf", "Lentor", "Mayflower", "Bright Hill", "Upper Thomson", "Caldecott", "Stevens", "Napier", "Orchard Boulevard", "Orchard", "Great World", "Havelock", "Outram Park", "Maxwell", "Shenton Way", "Marina Bay", "Gardens by the Bay"]
#
#
# station_lists = [
#     ("Red Line", nodeDist.mrt_list_generator(red_stations)),
#     ("Yellow Line", nodeDist.mrt_list_generator(yellow_stations)),
#     ("Yellow 1", nodeDist.mrt_list_generator(yellow_1)),
#     ("Yellow 2", nodeDist.mrt_list_generator(yellow_2)),
#     ("Purple Line", nodeDist.mrt_list_generator(purple_stations)),
#     ("Green Line", nodeDist.mrt_list_generator(green_stations)),
#     ("Green Main", nodeDist.mrt_list_generator(green_main)),
#     ("Green Extended", nodeDist.mrt_list_generator(green_extended)),
#     ("Blue Line", nodeDist.mrt_list_generator(blue_stations)),
#     ("Brown Line", nodeDist.mrt_list_generator(brown_stations)),
# ]
#
# # Creating an empty graph
# G = nx.Graph()
#
# # Creating an instance of the Graph class
# graph = Graph()
#
# line_info = {}  # Dictionary to store line information
#
# # Add all stations to the graph
# for line_name, stations in station_lists:
#     add_stations_to_graph(graph, G, line_info, stations, line_name)
#
# import matplotlib.pyplot as plt
#
# # Draw the graph
# plt.figure(figsize=(8,6))
# pos = nx.spring_layout(G)  # positions for all nodes
#
# # Nodes
# nx.draw_networkx_nodes(G, pos, node_size=500)
#
# # Edges
# nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1)
#
# # Labels
# nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
#
# plt.axis("off")
# plt.show()
#
# # User input for start and end stations
# start = input("Enter start station: ")
# end = input("Enter destination station: ")
#
# # Calculate shortest distance and path using Dijkstra's algorithm
# shortest_distance = graph.dijkstra(start, end)
# shortest_path = nx.dijkstra_path(G, start, end, weight='weight')
#
# print(f"The shortest distance from {start} to {end} is {shortest_distance} km.")
# print("The shortest path is:", ' -> '.join(shortest_path))
#
# # Get line information for each station in the shortest path
# print("Line information:")
# for i in range(len(shortest_path) - 1):
#     print(f"From {shortest_path[i]} to {shortest_path[i+1]}: {line_info[(shortest_path[i], shortest_path[i+1])]}")


import networkx as nx
import matplotlib.pyplot as plt

# Define MRT stations
red_stations = ['Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji', 'Marsiling', 'Woodlands', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang', 'Ang Mo Kio', 'Bishan', 'Braddell', 'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset', 'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South Pier']
yellow_stations = ['HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa', 'Kent Ridge', 'one-north', 'Buona Vista', 'Holland Village', 'Farrer Road', 'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon', 'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten', 'Stadium', 'Nicoll Highway', 'Promenade']
yellow_1 = ['Promenade', 'Bayfront', 'Marina Bay']
yellow_2 = ['Promenade', 'Esplanade', 'Bras Basah', 'Dhoby Ghaut']
purple_stations = ['HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng', 'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang', 'Punggol']

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = {}

    def add_edge(self, node1, node2, weight):
        self.nodes[node1][node2] = weight
        self.nodes[node2][node1] = weight

    def dijkstra(self, start_node, end_node):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_node] = 0
        visited = set()

        while len(visited) < len(self.nodes):
            current_node = None
            min_distance = float('inf')

            for node in self.nodes:
                if node not in visited and distances[node] < min_distance:
                    current_node = node
                    min_distance = distances[node]

            visited.add(current_node)

            if current_node == end_node:  # Exit the loop if the end node is reached
                break

            for neighbor, weight in self.nodes[current_node].items():
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances[end_node]


# Creating an empty graph
G = nx.Graph()

# Adding nodes to represent stations
G.add_nodes_from(red_stations, line='Red Line')
G.add_nodes_from(yellow_stations, line='Yellow Line')
G.add_nodes_from(yellow_1, line='Yellow Line')
G.add_nodes_from(yellow_2, line='Yellow Line')
G.add_nodes_from(purple_stations, line='Purple Line')

# Adding edges to represent connections between stations
red_line_edges = [(red_stations[i], red_stations[i+1]) for i in range(len(red_stations)-1)]
G.add_edges_from(red_line_edges)

yellow_line_edges = [(yellow_stations[i], yellow_stations[i+1]) for i in range(len(yellow_stations)-1)]
G.add_edges_from(yellow_line_edges)

yellow_1_edges = [(yellow_1[i], yellow_1[i+1]) for i in range(len(yellow_1)-1)]
G.add_edges_from(yellow_1_edges)

yellow_2_edges = [(yellow_2[i], yellow_2[i+1]) for i in range(len(yellow_2)-1)]
G.add_edges_from(yellow_2_edges)

purple_line_edges = [(purple_stations[i], purple_stations[i+1]) for i in range(len(purple_stations)-1)]
G.add_edges_from(purple_line_edges)


# Creating an instance of the Graph class
graph = Graph()

# Adding nodes and edges to the Graph class instance
for node in G.nodes():
    graph.add_node(node)

for edge in G.edges():
    weight = 1  # Assuming all edges have equal weight for simplicity
    graph.add_edge(edge[0], edge[1], weight)

# Source and destination MRT stations
source_station = 'Stadium'
destination_station = 'Dhoby Ghaut'

# Applying Dijkstra's algorithm to find the optimal path
distances = graph.dijkstra(source_station, destination_station)

# Getting the optimal path
shortest_path = nx.shortest_path(G, source_station, destination_station)

# Drawing the graph with highlighted optimal path
pos = nx.spring_layout(G, seed=42, scale=3, k=0.5)

# Draw the optimal path in blue
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)

# Printing the optimal path
print("Optimal Path: ", shortest_path)

node_colors = {'Red Line': 'red', 'Yellow Line': 'yellow', 'Purple Line': 'purple'}
node_color = [node_colors[data['line']] for _, data in G.nodes(data=True)]
nx.draw_networkx(G, pos, node_color=node_color, with_labels=True, node_size=200, edge_color='gray')
plt.title('Subway Lines - Optimal Path from {} to {}'.format(source_station, destination_station))
plt.show()




# station_distances = {}
#
# # Red Line stations
# for i in range(len(red_stations)-1):
#     station_distances[red_stations[i]] = 1  # Assuming distance between consecutive red line stations is 1
#
# # Yellow Line stations
# for i in range(len(yellow_stations)-1):
#     station_distances[yellow_stations[i]] = 1  # Assuming distance between consecutive yellow line stations is 1
#
# # Yellow 1 Line stations
# for i in range(len(yellow_1)-1):
#     station_distances[yellow_1[i]] = 1  # Assuming distance between consecutive yellow 1 line stations is 1
#
# # Yellow 2 Line stations
# for i in range(len(yellow_2)-1):
#     station_distances[yellow_2[i]] = 1  # Assuming distance between consecutive yellow 2 line stations is 1
#
# # Purple Line stations
# for i in range(len(purple_stations)-1):
#     station_distances[purple_stations[i]] = 1  # Assuming distance between consecutive purple line stations is 1
#
# # Print the station distances dictionary
# print(station_distances)
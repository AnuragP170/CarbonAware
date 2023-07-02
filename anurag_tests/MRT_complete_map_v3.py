import networkx as nx
import matplotlib.pyplot as plt
import node_distance_calculator as nodeDist # requires file called node_distance_calculator.py file to generate list/tuple data structure from arrays.

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

            if current_node is None:  # Exit the loop if no valid node is found
                break

            visited.add(current_node)

            if current_node == end_node:  # Exit the loop if the end node is reached
                break

            for neighbor, weight in self.nodes[current_node].items():
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances[end_node]


# red_stations = [('Jurong East', 'Bukit Batok', 2.7), ('Bukit Batok', 'Bukit Gombak', 1.9), ('Bukit Gombak', 'Choa Chu Kang', 4.2), ('Choa Chu Kang', 'Yew Tee', 1.6), ('Yew Tee', 'Kranji', 4.8), ('Kranji', 'Marsiling', 1.7), ('Marsiling', 'Woodlands', 1.4), ('Woodlands', 'Admiralty', 3.2), ('Admiralty', 'Sembawang', 2.7), ('Sembawang', 'Canberra', 3.9), ('Canberra', 'Yishun', 1.8), ('Yishun', 'Khatib', 1.8), ('Khatib', 'Yio Chu Kang', 5.5), ('Yio Chu Kang', 'Ang Mo Kio', 1.8), ('Ang Mo Kio', 'Bishan', 2.6), ('Bishan', 'Braddell', 2.1), ('Braddell', 'Toa Payoh', 1.0), ('Toa Payoh', 'Novena', 2.4), ('Novena', 'Newton', 2.2), ('Newton', 'Orchard', 1.1), ('Orchard', 'Somerset', 1.2), ('Somerset', 'Dhoby Ghaut', 1.2), ('Dhoby Ghaut', 'City Hall', 1.1), ('City Hall', 'Raffles Place', 1.6), ('Raffles Place', 'Marina Bay', 2.3), ('Marina Bay', 'Marina South Pier', 1.8)]
# yellow_stations = [('HarbourFront', 'Telok Blangah', 2.6), ('Telok Blangah', 'Labrador Park', 0.9), ('Labrador Park', 'Pasir Panjang', 1.4), ('Pasir Panjang', 'Haw Par Villa', 1.5), ('Haw Par Villa', 'Kent Ridge', 3.3), ('Kent Ridge', 'one-north', 3.3), ('one-north', 'Buona Vista', 0.9), ('Buona Vista', 'Holland Village', 1.1), ('Holland Village', 'Farrer Road', 2.2), ('Farrer Road', 'Botanic Gardens', 1.3), ('Botanic Gardens', 'Caldecott', 5.3), ('Caldecott', 'Marymount', 1.6), ('Marymount', 'Bishan', 1.9), ('Bishan', 'Lorong Chuan', 3.2), ('Lorong Chuan', 'Serangoon', 1.0), ('Serangoon', 'Bartley', 1.1), ('Bartley', 'Tai Seng', 1.9), ('Tai Seng', 'MacPherson', 2.1), ('MacPherson', 'Paya Lebar', 0.8), ('Paya Lebar', 'Dakota', 2.0), ('Dakota', 'Mountbatten', 1.6), ('Mountbatten', 'Stadium', 2.8), ('Stadium', 'Nicoll Highway', 2.9), ('Nicoll Highway', 'Promenade', 1.9)]


red_stations = ['Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji',
                'Marsiling', 'Woodlands', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang',
                'Ang Mo Kio', 'Bishan', 'Braddell', 'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset',
                'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South Pier']

yellow_stations = ['HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa', 'Kent Ridge', 'one-north', 'Buona Vista', 'Holland Village', 'Farrer Road', 'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon', 'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten', 'Stadium', 'Nicoll Highway', 'Promenade']
yellow_1 = ['Promenade', 'Bayfront', 'Marina Bay']
yellow_2 = ['Promenade', 'Esplanade', 'Bras Basah', 'Dhoby Ghaut']
purple_stations = ['HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng', 'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang', 'Punggol']
green_stations = ['Tuas Link', 'Tuas West Road', 'Tuas Crescent', 'Gul Circle', 'Joo Koon', 'Pioneer', 'Boon Lay', 'Lakeside', 'Chinese Garden', 'Jurong East', 'Clementi', 'Dover', 'Buona Vista', 'Commonwealth', 'Queenstown', 'Redhill', 'Tiong Bahru', 'Outram Park', 'Tanjong Pagar', 'Raffles Place', 'City Hall', 'Bugis', 'Lavender', 'Kallang', 'Aljunied', 'Paya Lebar', 'Eunos', 'Kembangan', 'Bedok', 'Tanah Merah']
green_main = ['Tanah Merah','Simei', 'Tampines', 'Pasir Ris']
green_extended = ['Tanah Merah','Expo', 'Changi Airport']
blue_stations = ["Bukit Panjang", "Cashew", "Hillview", "Beauty World", "King Albert Park", "Sixth Avenue", "Tan Kah Kee", "Botanic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis", "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen", "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit", "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi", "Expo"]
brown_stations = ["Woodlands North", "Woodlands", "Woodlands South", "Springleaf", "Lentor", "Mayflower", "Bright Hill", "Upper Thomson", "Caldecott", "Stevens", "Napier", "Orchard Boulevard", "Orchard", "Great World", "Havelock", "Outram Park", "Maxwell", "Shenton Way", "Marina Bay", "Gardens by the Bay"]

red_stations = nodeDist.mrt_list_generator(red_stations)
yellow_stations = nodeDist.mrt_list_generator(yellow_stations)
yellow_1 = nodeDist.mrt_list_generator(yellow_1)
yellow_2 = nodeDist.mrt_list_generator(yellow_2)
purple_stations = nodeDist.mrt_list_generator(purple_stations)
green_stations = nodeDist.mrt_list_generator(green_stations)
green_main = nodeDist.mrt_list_generator(green_main)
green_extended = nodeDist.mrt_list_generator(green_extended)
blue_stations = nodeDist.mrt_list_generator(blue_stations)
brown_stations = nodeDist.mrt_list_generator(brown_stations)

# Creating an empty graph
G = nx.Graph()

# Creating an instance of the Graph class
graph = Graph()

line_info = {}  # Dictionary to store line information

for edge in red_stations:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Red Line'  # Store line information

for edge in yellow_1:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Yellow Line'  # Store line information
for edge in yellow_2:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Yellow Line'  # Store line information

for edge in yellow_stations:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Yellow Line'  # Store line information

for edge in purple_stations:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Purple Line'  # Store line information

for edge in green_stations:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Green Line'  # Store line information

for edge in green_main:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Green Line'  # Store line information

for edge in green_extended:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Green Line'  # Store line information

for edge in blue_stations:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Blue Line'  # Store line information

for edge in brown_stations:
    G.add_edge(edge[0], edge[1], weight=edge[2])
    graph.add_node(edge[0])  # Add the source node
    graph.add_node(edge[1])  # Add the destination node
    graph.add_edge(edge[0], edge[1], edge[2])
    line_info[(edge[0], edge[1])] = 'Brown Line'  # Store line information


# Source and destination MRT stations
source_station = 'Serangoon'
destination_station = 'Changi Airport'

# Drawing the graph with highlighted optimal path
plt.figure(figsize=(20, 18))  # Set the size of the figure

# Applying Dijkstra's algorithm to find the optimal path
distances = graph.dijkstra(source_station, destination_station)

# Getting the optimal path
shortest_path = nx.shortest_path(G, source_station, destination_station, weight='weight')

# Drawing the graph with highlighted optimal path
pos = nx.spring_layout(G, seed=42, scale=9, k=0.4)

node_colors = {node: 'red' for node in graph.nodes if node in [station[0] for station in red_stations]}
node_colors.update({node: 'yellow' for node in graph.nodes if node in [station[0] for station in yellow_stations] or
                    node in [station[0] for station in yellow_1] or node in [station[0] for station in yellow_2]})
node_colors.update({node: 'purple' for node in graph.nodes if node in [station[0] for station in purple_stations]})
node_colors.update({node: 'green' for node in graph.nodes if node in [station[0] for station in green_stations] or
                    node in [station[0] for station in green_main] or node in [station[0] for station in green_extended]})
node_colors.update({node: 'blue' for node in graph.nodes if node in [station[0] for station in blue_stations]})
node_colors.update({node: 'brown' for node in graph.nodes if node in [station[0] for station in brown_stations]})
node_colors.update({'Marina South Pier': 'red', 'Promenade': 'yellow'})  # Add Marina South Pier and Promenade with blue color

# Draw the optimal path in blue
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='magenta', width=5)

# Printing the optimal path
print("Optimal Path:", shortest_path)

# Draw the graph with node and edge colors
nx.draw_networkx(G, pos, node_color=[node_colors.get(node, 'black') for node in G.nodes()], edge_color=[node_colors.get((node, node2), 'black') for node, node2 in G.edges()], with_labels=True, node_size=500, width=1)

# Draw nodes with labels
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)

plt.title('Subway Lines - Optimal Path from {} to {}'.format(source_station, destination_station))
plt.show()

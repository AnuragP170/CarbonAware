import networkx as nx
from pyvis.network import Network

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

# Creating a NetworkX graph
nx_graph = nx.Graph(G)

# Creating a Pyvis Network
pyvis_graph = Network(notebook=True)

# Define node colors
node_colors = {'Red Line': 'red', 'Yellow Line': 'yellow', 'Purple Line': 'purple'}

# Adding nodes with their attributes to the Pyvis Network
for node, data in nx_graph.nodes(data=True):
    pyvis_graph.add_node(node, color=node_colors[data['line']])

# Adding edges to the Pyvis Network
for edge in nx_graph.edges():
    pyvis_graph.add_edge(edge[0], edge[1])

# Highlighting the optimal path in the Pyvis Network
for i in range(len(shortest_path) - 1):
    pyvis_graph.add_edge(shortest_path[i], shortest_path[i+1], color='blue')

# Saving the Pyvis Network as an HTML file
pyvis_graph.show('graph.html')

import networkx as nx
import matplotlib.pyplot as plt

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

            for neighbor, weight in self.nodes[current_node].items():
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances[end_node]

# Example usage:
graph = Graph()

# Add nodes for each MRT station
stations = ['Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji', 'Marsiling', 'Woodlands', 'Admiralty', 'Sembawang', 'Yishun', 'Khatib', 'Yio Chu Kang', 'Ang Mo Kio', 'Bishan', 'Braddell', 'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset', 'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South Pier']
for station in stations:
    graph.add_node(station)

# Add edges between each station with arbitrary weights
for i in range(len(stations) - 1):
    graph.add_edge(stations[i], stations[i + 1], i + 1)

# Run Dijkstra's algorithm and get the optimal path
start_node = 'Jurong East'
end_node = 'Ang Mo Kio'
shortest_distance = graph.dijkstra(start_node, end_node)

# Create a NetworkX graph
nx_graph = nx.Graph()
for node, neighbors in graph.nodes.items():
    nx_graph.add_node(node)
    for neighbor, weight in neighbors.items():
        nx_graph.add_edge(node, neighbor, weight=weight)

# Get the nodes and edges of the optimal path
shortest_path = nx.shortest_path(nx_graph, start_node, end_node, weight='weight')

# Choose a layout algorithm (e.g., shell_layout, circular_layout, spectral_layout)
pos = nx.shell_layout(nx_graph)  # You can try different layout algorithms here

# Draw the graph using NetworkX
nx.draw(nx_graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
labels = nx.get_edge_attributes(nx_graph, 'weight')
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=labels)

# Highlight the nodes and edges of the optimal path
nx.draw_networkx_nodes(nx_graph, pos, nodelist=shortest_path, node_color='red', node_size=500)
for i in range(len(shortest_path) - 1):
    nx.draw_networkx_edges(nx_graph, pos, edgelist=[(shortest_path[i], shortest_path[i + 1])], edge_color='red', width=2)

# Show the graph
plt.show()

print(f"The shortest distance between {start_node} and {end_node} is: {shortest_distance}")
print(f"The optimal path is: {shortest_path}")

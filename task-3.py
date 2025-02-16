import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Add edge to the graph
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)  # For undirected graph
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight  # For undirected graph

def dijkstra(graph, initial):
    # Distances dictionary
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[initial] = 0

    # Priority queue of vertices
    pq = [(0, initial)]

    # Previous vertex dictionary for path reconstruction
    previous = {vertex: None for vertex in graph.edges}

    # Set of visited vertices
    visited = set()

    while pq:
        # Get vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(pq)

        # If we've already visited this vertex, skip it
        if current_vertex in visited:
            continue

        # Mark vertex as visited
        visited.add(current_vertex)

        # Check all adjacent vertices
        for neighbor in graph.edges[current_vertex]:
            if neighbor in visited:
                continue

            # Calculate new distance to neighbor
            weight = graph.weights[(current_vertex, neighbor)]
            distance = current_distance + weight

            # If we've found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

def get_path(previous, target):
    """Reconstruct path from source to target using previous dictionary"""
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    return path[::-1]  # Reverse path to get it from source to target

# Example usage
def test_dijkstra():
    # Create a sample graph
    g = Graph()

    # Add edges (you can modify these values to test different graphs)
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)

    # Run Dijkstra's algorithm from vertex 'A'
    distances, previous = dijkstra(g, 'A')

    # Print results
    print("Shortest distances from vertex A:")
    for vertex in sorted(distances):
        print(f"To {vertex}: {distances[vertex]}")
        path = get_path(previous, vertex)
        print(f"Path: {' -> '.join(path)}")
        print()

if __name__ == "__main__":
    test_dijkstra()
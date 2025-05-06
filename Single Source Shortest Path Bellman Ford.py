def bellman_ford(graph, vertices, source):
    distance = {i: float('inf') for i in range(vertices)}
    predecessor = {i: None for i in range(vertices)}
    distance[source] = 0

    for _ in range(vertices - 1):
        for u, v, w in graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    for u, v, w in graph:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains negative weight cycle")
            return distance, predecessor, True

    return distance, predecessor, False

def print_path(predecessor, destination):
    if predecessor[destination] is None:
        print(destination, end="")
        return
    print_path(predecessor, predecessor[destination])
    print(f" -> {destination}", end="")

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    graph = []
    print(f"Enter {edges} edges in the format: u v weight")
    for _ in range(edges):
        u, v, w = map(int, input("Edge: ").split())
        graph.append((u, v, w))

    source = int(input("Enter the source vertex: "))

    distances, predecessors, negative_cycle = bellman_ford(graph, vertices, source)

    if not negative_cycle:
        print(f"\nShortest distances from source vertex {source}:")
        for vertex in range(vertices):
            print(f"Vertex {vertex}: Distance = {distances[vertex]}", end="")
            if distances[vertex] != float('inf'):
                print(", Path: ", end="")
                print_path(predecessors, vertex)
            print()

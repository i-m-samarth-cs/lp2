import heapq

def dijkstra(graph, start, dest):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    predecessors = {node: None for node in graph}

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = curr_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    current = dest
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()

    return distances, path

# Input from user
v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(v)}  # Initialize graph for 0 to v-1

print("Enter edges in the format: u v w (space separated)")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # For undirected graph

start = int(input("Enter the starting vertex: "))
dest = int(input("Enter the destination vertex: "))

# Run Dijkstra's algorithm
shortest_distances, path = dijkstra(graph, start, dest)

# Output

print(f"Shortest path from {start} to {dest}: {' -> '.join(map(str, path))}")
print(f"\nShortest distance from {start} to {dest} = {shortest_distances[dest]}")

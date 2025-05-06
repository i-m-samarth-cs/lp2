import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Input from user
v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {}
for i in range(1, v + 1):
    graph[i] = []

print("Enter edges in the format: u v w")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start = int(input("Enter the starting vertex: "))

# Run Dijkstra's algorithm
shortest_distances = dijkstra(graph, start)

# Output
print("\nShortest distances from node", start)
for node in sorted(shortest_distances):
    print(f"From {start} to {node} = {shortest_distances[node]}")

import heapq  # priority queue साठी

def prim(n, adj):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node) — node 0 पासून सुरू
    total_cost = 0
    mst = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight

        if weight != 0:
            mst.append((u, weight))

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    print("\n Minimum Spanning Tree edges:")
    for u, w in mst:
        print(f"{u + 1} (weight = {w})")  # Output मध्ये 1-based index
    print(f"Total Minimum Cost = {total_cost}")

#  User Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

adj = [[] for _ in range(n)]
print("Enter edges (format: u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    u -= 1  # Convert to 0-based
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))  # undirected graph

# Run Prim's Algorithm
prim(n, adj)

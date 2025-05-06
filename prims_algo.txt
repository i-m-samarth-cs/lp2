import heapq

def prims_mst(graph, vertices, start_vertex=0):
    pq, visited, mst_edges, total_weight = [(0, start_vertex, None)], [False] * vertices, [], 0
    while pq:
        weight, current, parent = heapq.heappop(pq)
        if visited[current]: continue
        visited[current] = True
        if parent is not None: mst_edges.append((parent, current, weight)); total_weight += weight
        for neighbor, edge_weight in graph[current]:
            if not visited[neighbor]: heapq.heappush(pq, (edge_weight, neighbor, current))
    return mst_edges, total_weight

if __name__ == "__main__":
    vertices = int(input("Enter number of vertices: "))
    
    graph = {i: [] for i in range(vertices)}
    
    edges = int(input("Enter number of edges: "))
    
    for _ in range(edges):
        u, v = map(int, input("Enter edge (vertex1 vertex2): ").split())
        weight = int(input(f"Enter weight for edge ({u} - {v}): "))
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # As it's an undirected graph
    
    start_vertex = int(input("Enter starting vertex: "))
    
    mst_edges, total_weight = prims_mst(graph, vertices, start_vertex)
    
    print("\nEdges in MST:")
    for parent, vertex, weight in mst_edges:
        print(f"({parent} - {vertex}) with weight {weight}")
    print(f"\nTotal weight of MST: {total_weight}")

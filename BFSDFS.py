def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set()
    visited2 = set()
    queue = []

    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        graph[i] = []

    e = int(input("Enter number of edges: "))
    print("Enter edges (u v) one per line:")
    for _ in range(e):
        u, v = map(int, input().split())
        if u not in graph or v not in graph:
            print(f"Invalid edge ({u}, {v}) - Node out of range.")
            continue
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph

    start = int(input("Enter starting node: "))
    if start not in graph:
        print(f"Starting node {start} is invalid.")
        return

    print("\nThe following is DFS")
    dfs(visited1, graph, start)
    print("\nThe following is BFS")
    bfs(visited2, graph, start, queue)

if __name__ == "__main__":
    main()


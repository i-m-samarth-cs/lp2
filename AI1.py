
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        # Use .get() to safely get neighbors even if node doesn't exist
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" 0")
        for neighbour in graph.get(s, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set()
    visited2 = set()
    queue = []
    n = int(input("Enter number of nodes: "))

    # Initialize graph with all nodes (even if they have no edges)
    graph = {i: [] for i in range(1, n + 1)}

    # Read edges
    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

            # Optional: if undirected, add the reverse edge
            # graph[node].append(i)

    print("\nThe following is DFS:")
    dfs(visited1, graph, 1)

    print("\n\nThe following is BFS:")
    bfs(visited2, graph, 1, queue)

if __name__ == "__main__":
    main()


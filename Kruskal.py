class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent, rank):
    parA = find(a, parent)
    parB = find(b, parent)
    if parA == parB:
        return
    if rank[parA] < rank[parB]:
        parent[parA] = parB
    elif rank[parB] < rank[parA]:
        parent[parB] = parA
    else:
        parent[parB] = parA
        rank[parA] += 1

def initialize_union_find(V):
    parent = [i for i in range(V + 1)]
    rank = [0] * (V + 1)
    return parent, rank

def kruskals_mst(edges, V):
    edges.sort(key=lambda e: e.wt)
    parent, rank = initialize_union_find(V)

    mst_weight = 0
    count = 0
    mst_edges = []  # ✅ Store selected edges here

    for edge in edges:
        if count == V - 1:
            break
        parA = find(edge.src, parent)
        parB = find(edge.dest, parent)
        if parA != parB:
            union(edge.src, edge.dest, parent, rank)
            mst_weight += edge.wt
            mst_edges.append(edge)  # ✅ Add edge to result
            count += 1

    return mst_weight, mst_edges  # ✅ Return both

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))

    edges = []
    print("Enter each edge as: src dest weight")
    for _ in range(e):
        s, d, w = map(int, input().split())
        edges.append(Edge(s, d, w))

    mst_weight, mst_edges = kruskals_mst(edges, n)

    print("Total cost of MST:", mst_weight)
    print("Edges in the MST:")
    for edge in mst_edges:
        print(f"{edge.src} -- {edge.dest} == {edge.wt}")


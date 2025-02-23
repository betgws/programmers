def solution(n, costs):
    costs.sort(key=lambda x:x[2])

    parent = [i for i in range(n)]

    rank = [0]*n
    total_cost = 0
    edge_count = 0

    for u,v,cost in costs:
        if(find(parent, u) != find(parent, v)):
            union(parent,rank,u,v)
            total_cost = total_cost+cost
            edge_count = edge_count + 1

            if edge_count == n - 1:
                break

    return total_cost

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent,a)
    rootB = find(parent,b)

    if(rootA != rootB):
        if(rank[rootA] > rank[rootB]):
            parent[rootB] = rootA

        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB

        else:
            parent[rootB] = rootA
            rank[rootA] += 1
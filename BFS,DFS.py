from collections import defaultdict, deque

N, M, V = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

dic = defaultdict(list)

# 무방향 그래프
for i, j in A:
    dic[i].append(j)
    dic[j].append(i)

# 각 인접 리스트 정렬 (번호 작은 정점부터 방문하기 위함)
for k in dic:
    dic[k].sort()

# DFS
visited = [False] * N
dfs_order = []

def Dfs(start):
    visited[start - 1] = True
    dfs_order.append(start)
    for i in dic[start]:
        if not visited[i - 1]:
            Dfs(i)

# BFS
def Bfs(start):
    visited = [False] * N
    order = []
    q = deque([start])
    visited[start - 1] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in dic[u]:
            if not visited[v - 1]:
                visited[v - 1] = True
                q.append(v)
    return order

Dfs(V)
print(*dfs_order)
print(*Bfs(V))

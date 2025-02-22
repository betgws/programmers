import heapq

def solution(n,cost):

    graph = {i: [] for i in range(n)}

    for u,v,cost in cost:
        graph[u].append((cost,v))
        graph[v].append((cost,u))


    visited = set()
    min_heap = [(0,0)]
    answer = 0 

    while(len(visited) < n):
        cost, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            answer = answer + cost
            for next_cost, v in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap,(next_cost,v))

    return answer


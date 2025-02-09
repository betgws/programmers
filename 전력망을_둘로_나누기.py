
from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])
   
    visited[start] = True
    cnt = 0

    while queue:
        
        v = queue.popleft()
        
        cnt += 1
       
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt

def bfs(graph, index, visited):
    queue = deque()

    queue.append(index)
    visited[index] = True

    cnt = 1
    while(queue):
        v = queue.popleft()
        for i in graph[v]:
            if(visited[i] == False):
                visited[i] = True
                cnt = cnt + 1
                queue.append(i)
    return cnt

def solution(n, wires):
    answer = n - 2 
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tmps.pop(i) # i번째 전선 제거
        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx,g in enumerate(graph):
            if g != []: 
                start = idx
                break
        cnts = bfs(graph, start, visited)
        other_cnts = n - cnts 
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)

    
    return answer

solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])


def solution(n,wires):
    for i in range(n):
        tmp = wires.copy()
        tmp.pop(i)
        graph= [[] for _ in range(n+1)]
        visited = [False]*(n+1)

        for i in wires:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        for index,a in enumerate(graph):
            if a:
                cnt = bfs(index,graph,visited)
                break
        anwer

def bfs(index, graph, visited):
    queue = deque()
    queue.append(index)

    while(queue):
        cnt = cnt + 1
        v = queue.popleft()
        for i in graph[v]:
            if (visited[i] == False):
                queue.append(i)
                visited[i] = True







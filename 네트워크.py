from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(index):
        queue = deque([index])
        while queue:
            v = queue.popleft()
            for ind, connected in enumerate(computers[v]):
                if connected == 1 and not visited[ind]:
                    visited[ind] = True
                    queue.append(ind)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])

def soltion(n, computer):
    answer = 0 
    visited = [False]*n

    def dfs(i):
        queue = deque([i])

        while queue:
            q = queue.popleft()
            for ind, k in enumerate(computer[q]):
                if k[ind] == 1 and visited[ind] == False:
                    queue.append(ind)
                    visited[ind] = True

    for i in range(0,n):
        if(visited[i] == False):
            dfs(i)
            answer = answer + 1
    

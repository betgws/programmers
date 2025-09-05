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

def solution1(n, computers):
    visited = [False]*n
    answer = 0

    def BFS(startInd):
        queue = deque()
        queue.append(startInd)
        visited[startInd] = True

        while queue:
            j = queue.popleft()
            for index,i in enumerate(computers[j]):
                if(i == 1 and visited[index] == False):
                    visited[index] == True
                    queue.append(index)

    for i in range(n):
        if(visited[i] == False):
            BFS(i)
            answer += 1


def solution3(n,computer):
    visited = [False]*n

    def dfs(v):
        visited[v] = True
        for ind, i in enumerate(computer[v]):
            if(visited[ind] != True and i == 1):
                dfs(i)

    answer = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

        return answer 
    

def solution4(n,computer):
    visited = [False]*n

    def bfs(start):
        q = deque([start])
        visited[start] = True
        while q:
            v = q.popleft()
            for i in range(n):
                if computer[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append[i]
                    




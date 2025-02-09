from collections import deque

def solution(n, computers):
    
    answer = []
    visited= [False] * (n+1)
    inList = []

    for i in range(n):
        if(i not in inList):
            cnt = bfs(i,computers,visited)
            answer.append(cnt)
            for i in cnt:
                inList.append(i)

    
    
    return len(answer)

def bfs(index, computers, visited):

    queue = deque()
    queue.append(index)
    visited[index] = True
    cnt = [index]

    while(queue):
        v = queue.popleft()
        for ind ,a in enumerate(computers[v]):
            if a == 1 and visited[ind] == False:
                queue.append(ind)
                cnt.append(ind)
                visited[ind] = True

    return cnt

solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])



    

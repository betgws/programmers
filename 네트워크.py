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
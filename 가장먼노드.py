from collections import deque

def solution(n, edge):
    graph = [([0]*n) for _ in range(n)]
    visitied = [False]*n

    for i in edge:
        graph[i[0]-1][i[1]-1] = 1
        graph[i[1]-1][i[0]-1] = 1

    def BFS(start):
        queue = deque()
        visitied[start] = True 
        answer = [0] * n  

        queue.append((start, 0))

        while queue:
            node, dist = queue.popleft()
            for indx, isConnected in enumerate(graph[node]):
                if visitied[indx] == False and isConnected == 1:
                    visitied[indx] = True
                    queue.append((indx, dist + 1))
                    answer[indx] = dist + 1 

        max_dist = max(answer)
        return answer.count(max_dist)

    return BFS(0)

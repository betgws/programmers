from collections import deque

def solution(n, edge):

    graph = [[] for _ in range(n+1)]
    visited =[False]*(n+1)
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    answer  = bfs(visited,graph,1,n)
    return answer

def bfs(visited, graph,start,n):

    queue = deque()
    a = 1
    lef = 0
    answer =  0
    max = 0
    visited[start] = True
    for i in graph[start]:
        queue.append((i,a))
        visited[i] = True

    while(queue):
        pop1 = queue.popleft()

        for j in graph[pop1[0]]:
            if(visited[j]!=True):
                visited[j] = True
                queue.append((j,pop1[1]+1))
            else:
                lef = lef+1

        if(lef == len(graph[pop1[0]])):
            if(max < pop1[1]):
                max = pop1[1]
                answer = 1

            elif(max == pop1[1]):
                answer = answer + 1

        lef = 0

    return answer

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
                




from collections import deque

N,M = map(int,input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

# 최소 칸수니까 BFS

# 동,서,남,북
dir = [(0,1),(0,-1),(1,0),(-1,0)]

# 이미 간 곳
visited = [[False]*M for i in range(N)]

def bfs(start):
    queue = deque()
    queue.append([start, 1])
    visited[start[0]-1][start[1]-1] = True

    while queue:

        loLIst, cnt = queue.popleft()
        loR, loS = loLIst[0], loLIst[1]


        for r,s in dir:
            nr = loR + r 
            ns = loS + s 
            if(nr == N and ns == M):
                return cnt + 1
            if 0 <= nr-1 < N and 0 <= ns-1 < M:
                if(board[nr-1][ns-1] == 1 and visited[nr-1][ns-1] != True):
                    queue.append([[nr,ns], cnt+1])
                    visited[nr-1][ns-1] = True



answer = bfs([1,1])

print(answer)
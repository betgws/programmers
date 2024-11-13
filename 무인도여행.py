from collections import deque

def solution(maps):

    n,m = len(maps), len(maps[0])
    visit = [[0]* m for _ in range(n)]
    answer = []

    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and maps[i][j] != 'X':
                answer.append(bfs(i,j,n,m,visit,maps))

    if areas:
        return sorted(answer)
    else:
        return [-1]
    

def bfs(i,j,n,m,visit,maps):

    queue = deque()
    queue.append((i,j))
    visit[i][j] = 1
    areas = int(map[i][j])

    while queue:
        x,y = queue.popleft()
        for b in range(4): 
            nx, ny =  x + dx[b], y + dy[b]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0  and maps[nx][ny] != 'X':
                visit[nx][ny] = 1
                areas = areas + int(maps[nx][ny])
                queue.append((nx,ny))
    return areas
  




from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])
    answer = []

    visitisland = [[0]*m for _ in range(n)]

    for i in range (n):
        for j in range(m):
            if visitisland[i][j] ==  0 and maps[i][j] != "X":
                answer.append(countCloseIslane(maps,visitisland,i,j,n,m))

    return answer


dy = [0,0,1,-1] 
dx = [1,-1,0,0]


def countCloseIslane(maps, visit,i,j,n,m):

    queue = deque()
    queue.append((i,j))
    areas = 0
    visit
    while(queue):

        i,j = queue.popleft()

        for a in range(4):

            nx = i + dx[a]
            ny = j + dy[a]

            if( 0<= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and maps[nx][ny] !="X"):
                queue.append((nx,ny))
                visit[nx][ny] == 1
                areas = areas + int(maps[nx][ny])



    return areas 





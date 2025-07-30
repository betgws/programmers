from itertools import combinations
from collections import deque
import copy

N,M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]


def bfs(lab, virus_list):
    q = deque(virus_list)
    dir = [(-1,0),(1,0),(0,-1),(0,1)]

    while q: 
        x , y = q.popleft()
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                q.append((nx,ny))

    return sum(row.count(0) for row in lab)



empty = []
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i,j))
        elif lab[i][j] == 2:
            virus.append((i,j))
max_safe = 0
for walls in combinations(empty,3):
    temp = copy.deepcopy(lab)
    for x,y in walls :
        temp[x][y] = 1

    sefe = bfs(temp, virus)
    max_safe = max(max_safe,sefe)



import heapq

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
max_sum = 0  # 최종 결과

for sr in range(N):
    for sc in range(M):
        canGo = []
        visitedBoard = [[False]*M for _ in range(N)]
        visitedBoard[sr][sc] = True
        visited = [(sr, sc)]

        total = board[sr][sc]  # 합계 시작

        while len(visited) < 4:
            r, c = visited[-1]

            # 인접한 후보들을 힙에 추가
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < M and not visitedBoard[nr][nc]:
                    heapq.heappush(canGo, (-board[nr][nc], (nr, nc)))

            if not canGo:
                break

            val, (nr, nc) = heapq.heappop(canGo)
            val = -val
            visitedBoard[nr][nc] = True
            visited.append((nr, nc))
            total += val

        if len(visited) == 4:
            max_sum = max(max_sum, total)

print(max_sum)
import heapq

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
max_sum = 0  # 최종 결과

for sr in range(N):
    for sc in range(M):
        canGo = []
        visitedBoard = [[False]*M for _ in range(N)]
        visitedBoard[sr][sc] = True
        visited = [(sr, sc)]

        total = board[sr][sc]  # 합계 시작

        while len(visited) < 4:
            r, c = visited[-1]

            # 인접한 후보들을 힙에 추가
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < M and not visitedBoard[nr][nc]:
                    heapq.heappush(canGo, (-board[nr][nc], (nr, nc)))

            if not canGo:
                break

            val, (nr, nc) = heapq.heappop(canGo)
            val = -val
            visitedBoard[nr][nc] = True
            visited.append((nr, nc))
            total += val

        if len(visited) == 4:
            max_sum = max(max_sum, total)

print(max_sum)


import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
max_sum = 0
visited = [[False]*M for _ in range(N)]

def dfs(r, c, depth, total):
    """DFS로 4칸 경로 탐색"""
    global max_sum
    if depth == 4:
        max_sum = max(max_sum, total)
        return

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, depth+1, total+board[nr][nc])
            visited[nr][nc] = False

def check_t_shape(r, c):
    """ㅗ 모양 (분기 모양) 체크"""
    global max_sum
    # 현재 중심(r,c)에서 네 방향 중 3방향을 선택
    center = board[r][c]
    for excluded in range(4):
        total = center
        valid = True
        for i, (dr, dc) in enumerate(dirs):
            if i == excluded:  # 한 방향 제외
                continue
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < M):
                valid = False
                break
            total += board[nr][nc]
        if valid:
            max_sum = max(max_sum, total)

for r in range(N):
    for c in range(M):
        # DFS로 4칸 탐색
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False

        # "ㅗ" 모양 체크
        check_t_shape(r, c)

print(max_sum)

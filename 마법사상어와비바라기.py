N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input.split())) for _ in range(M)]

# 방향

direction = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
water = [(-1,-1),(-1,1),(1,1),(1,-1)]

#초기 구름 위치 
start = [(N-1,0),(N-1,1),(N-2,0), (N-2,1)]

for d, s in moves:
    d = d - 1 #방향 인덱스 
    dr, dc = direction[d]

    # 1번 구름 이동(토리스 구조 적용)
    newCloud = []
    for r,c in start:
        nr = (r + dr * s) % N
        nc = (r + dc * s) % N 
        newCloud.append((nr,nc))
        A[nr][nc] += 1
    
    start = newCloud

    # 물복사 버그 
    for r,c in start:
        for dr,dc in water:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                A[r][c] += 1

    # 새 구름 생성 (이번 구름 위치 제외 하고, 물 - 2)
    cloud_set = set(start)
    newCloud = []
    for r in range(N):
        for c in range(N):
            if (r,c) in cloud_set:
                continue
            if A[r][c] >= 2:
                newCloud.append((r,c))
                A[r][c] -= 2
    start = newCloud
            

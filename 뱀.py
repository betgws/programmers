from collections import deque

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]

# 사과 위치 표시
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1  # 사과 있는 칸은 1로 표시

L = int(input())
turns = deque()
for _ in range(L):
    X, C = input().split()
    turns.append((int(X), C))

# 방향 (오른쪽, 아래, 왼쪽, 위)
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
dir_idx = 0  # 현재 방향 (오른쪽부터 시작)
time = 0

snake = deque([(0,0)])  # 뱀의 몸 (머리=맨끝)

while True:
    time += 1
    head_r, head_c = snake[-1]
    dr, dc = dirs[dir_idx]
    nr, nc = head_r + dr, head_c + dc

    # 벽이나 자기 몸과 부딪히면 종료
    if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in snake:
        print(time)
        break

    # 머리 이동
    snake.append((nr, nc))

    # 사과 있으면 꼬리 그대로, 없으면 꼬리 제거
    if board[nr][nc] == 1:
        board[nr][nc] = 0
    else:
        snake.popleft()

    # 방향 전환 시점
    if turns and time == turns[0][0]:
        _, C = turns.popleft()
        if C == 'L':
            dir_idx = (dir_idx - 1) % 4
        else:
            dir_idx = (dir_idx + 1) % 4



dirs = [(0,1),(1,0),(0,-1),(-1,0)]
dir_indx = 0
time = 0 

snake = deque([(0,0)])

while True:
    time += 1 
    head_r, head_c = snake[-1]
    dr , dc = dirs[dir_idx]
    nr, nc = dr + head_r , dc + head_c

    if not ( 0< nr <= N and 0 < nc <= N ) or (nr,nc) in snake:
        print(time)
        break 

    
    snake.append((nr,nc))

    if board[nr][nc] == 1:
        board[nr][nc] = 0

    else:
        snake.popleft()

    if turns and turns[0][0] == time:
        _, C = turns.popleft()
        if C == 'L':
            dir_idx = (dir_idx - 1) % 4
        else:
            dir_idx = (dir_idx + 1) % 4



N,M,r,c,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int,input().split()))

 
# 위 아래 북 남 서 동
dice = [0]*6

# 방향 정의 동서북남
dir = [(0,1),(0,-1),(-1,0),(1,0)]

def roll(direction):
    top, bottom, north, south, west, east = dice
    if direction == 1:  # 동쪽
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, top
    elif direction == 2:  # 서쪽
        dice[0], dice[1], dice[4], dice[5] = east, west, top, bottom
    elif direction == 3:  # 북쪽
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif direction == 4:  # 남쪽
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top

for cmd in command:
    nr =  r + dir[cmd][0]
    nc = c + dir[cmd][1]

    if not (0 <= nr < N and 0 <= nc < M):
        continue


    r, c = nr, nc


    roll(cmd)


    if board[x][y] == 0:
        board[x][y] = dice[1]  
    else:
        dice[1] = board[x][y] 
        board[x][y] = 0


    print(dice[0])

    
        

